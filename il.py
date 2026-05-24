#!/usr/bin/env python3
"""
DeFi Impermanent Loss Calculator - Calculate impermanent loss for liquidity pools
Helps LPs understand the risks of providing liquidity

BTC Tips: 1KPUa9Njq86NJwmwqVmdjZ4oC8eHrXKqf9
"""
import json
import urllib.request
import sys
from datetime import datetime
import math

def calculate_impermanent_loss(price_ratio):
    """
    Calculate impermanent loss based on price ratio change
    price_ratio = current_price / initial_price
    """
    if price_ratio <= 0:
        return 0
    
    # IL formula: 2 * sqrt(price_ratio) / (1 + price_ratio) - 1
    il = (2 * math.sqrt(price_ratio)) / (1 + price_ratio) - 1
    return abs(il) * 100  # Return as percentage

def display_il_calculator():
    """Display impermanent loss calculations"""
    print("=" * 70)
    print("DEFI IMPERMANENT LOSS CALCULATOR")
    print(f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    print(f"\n{'Price Change':<15} {'IL %':>8} {'Break-Even Fee':>15}")
    print("-" * 40)
    
    for change in [0.5, 0.25, 0.1, 1.0, 2.0, 3.0, 5.0]:
        il = calculate_impermanent_loss(change)
        # Break-even fee is the fee needed to offset IL
        break_even = il * 0.5  # Simplified estimate
        
        print(f"{change:>10}x {'':>5} {il:>7.2f}% {break_even:>13.2f}%")
    
    print(f"\nBTC Tips: 1KPUa9Njq86NJwmwqVmdjZ4oC8eHrXKqf9")

def main():
    display_il_calculator()

if __name__ == "__main__":
    main()
