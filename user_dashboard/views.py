from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import TraderData, AdminDashboardData
from .forms import TraderForm
from django.db.models import Q
import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import io
from django.http import FileResponse
from django.template.loader import get_template
from django.views import View
from django.template.loader import render_to_string
from xhtml2pdf import pisa


def generate_trader_data():
    traders = TraderData.objects.all()
    trader_data = {}
    for trader in traders:
        data_points = trader.profit_loss
        trader_data[trader.trader] = [profit_loss for profit_loss in data_points]
    return trader_data


# @login_required(login_url='login')
def dashboard(request):
    if request.method == 'POST':
        form = TraderForm(request.POST)
        if form.is_valid():
            trader_name = form.cleaned_data['trader']
            amount = form.cleaned_data['amount']
            profit_loss = []
            for minute in range(60):
                profit_loss.append(round(random.uniform(-100, 100), 2))
            trader = TraderData(trader=trader_name, amount=amount, profit_loss=profit_loss)
            trader.save()
            return redirect('dashboard')
    else:
        form = TraderForm()
    traders = TraderData.objects.all()
    trader_data = generate_trader_data()
    context = {
        'trader_data': trader_data,
        'traders': traders,
        'form': form,
    }
    return render(request, 'user_dashboard/dashboard.html', context)


# @login_required(login_url='login')
def admin_dashboard(request):
    trader_data = generate_trader_data()
    # Calculate the necessary data for the admin dashboard
    total_profit = 0
    total_loss = 0
    highest_profit = float('-inf')
    lowest_profit = float('inf')
    highest_profit_trader = ""
    lowest_profit_trader = ""
    timestamp = ""
    for trader, data_points in trader_data.items():
        total_profit += sum(profit_loss for profit_loss in data_points if profit_loss > 0)
        total_loss += sum(profit_loss for profit_loss in data_points if profit_loss < 0)
        trader_profit = sum(profit_loss for profit_loss in data_points)
        if trader_profit > highest_profit:
            highest_profit = trader_profit
            highest_profit_trader = trader
        if trader_profit < lowest_profit:
            lowest_profit = trader_profit
            lowest_profit_trader = trader
    # Save the admin dashboard data to the database
    admin_dashboard_data = AdminDashboardData.objects.create(
        total_profit=total_profit,
        total_loss=total_loss,
        highest_profit_trader=highest_profit_trader,
        lowest_profit_trader=lowest_profit_trader,
        timestamp=timestamp,
    )
    context = {
        'admin_dashboard_data': admin_dashboard_data
    }
    return render(request, 'user_dashboard/admin_dashboard.html', context)


class AdminDashboardPDFView(LoginRequiredMixin, View):
    def get(self, request):
        trader_data = generate_trader_data()
        total_profit = 0
        total_loss = 0
        highest_profit = float('-inf')
        lowest_profit = float('inf')
        highest_profit_trader = ""
        lowest_profit_trader = ""
        timestamp = ""
        for trader, data_points in trader_data.items():
            total_profit += sum(profit_loss for profit_loss in data_points if profit_loss > 0)
            total_loss += sum(profit_loss for profit_loss in data_points if profit_loss < 0)
            trader_profit = sum(profit_loss for profit_loss in data_points)
            if trader_profit > highest_profit:
                highest_profit = trader_profit
                highest_profit_trader = trader
            if trader_profit < lowest_profit:
                lowest_profit = trader_profit
                lowest_profit_trader = trader
        admin_dashboard_data = AdminDashboardData.objects.create(
            total_profit=total_profit,
            total_loss=total_loss,
            highest_profit_trader=highest_profit_trader,
            lowest_profit_trader=lowest_profit_trader,
            timestamp=timestamp,
        )
        template = get_template('user_dashboard/admin_dashboard_pdf.html')
        context = {
            'admin_dashboard_data': admin_dashboard_data
        }
        html = template.render(context)
        # Create a file-like buffer to receive PDF data
        buffer = io.BytesIO()
        # Create the PDF object using the buffer
        pisa.CreatePDF(html, dest=buffer)
        # Rewind the buffer's file pointer
        buffer.seek(0)
        # Set the content type of the response as PDF
        response = FileResponse(buffer, content_type='application/pdf')
        # Specify the filename for the downloaded PDF
        # response['Content-Disposition'] = 'attachment; filename="admin_dashboard.pdf"'
        response['Content-Disposition'] = 'inline; filename="admin_dashboard.pdf"'  # Set to "inline" to open in browser
        return response


@login_required(login_url='login')
def search(request):
    query = request.GET.get('query')
    results = []
    if query:
        results = TraderData.objects.filter(
            Q(trader__icontains=query)
            #  | Q(description__icontains=query)
        )
    context = {
        'query': query,
        'results': results
    }
    return render(request, 'user_dashboard/search.html', context)
