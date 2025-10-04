#!/bin/bash

BASE_URL="http://localhost:8000"

echo "🦖 Testing Historical Events Endpoints (English)..."
echo "=================================================="

# 1. All events
echo "1. All historical events:"
curl -s "$BASE_URL/historical/events" | python3 -m json.tool
echo ""

# 2. Search dinosaurs
echo "2. Searching 'dinosaurs':"
curl -s "$BASE_URL/historical/events/search?query=dinosaurs" | python3 -m json.tool
echo ""

# 3. Specific event
echo "3. Event ID 1 (Dinosaur extinction):"
curl -s "$BASE_URL/historical/events/1" | python3 -m json.tool
echo ""

# 4. Search Russia
echo "4. Searching 'russia':"
curl -s "$BASE_URL/historical/events/search?query=russia" | python3 -m json.tool
echo ""

echo "✅ Historical endpoints test completed!"
