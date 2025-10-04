#!/bin/bash

BASE_URL="http://localhost:8001"

echo "🔍 Detailed Testing NASA Asteroids API..."
echo "=========================================="

# 1. Health Check
echo "1. Testing Health Check:"
echo "URL: $BASE_URL/"
curl -s -X GET "$BASE_URL/"
echo ""
echo "----------------------------------------"
echo ""

# 2. Asteroid Feed
echo "2. Testing Asteroid Feed:"
echo "URL: $BASE_URL/asteroids/feed?start_date=2024-01-01&end_date=2024-01-02"
curl -s -X GET "$BASE_URL/asteroids/feed?start_date=2024-01-01&end_date=2024-01-02"
echo ""
echo "----------------------------------------"
echo ""

# 3. Get specific asteroid
echo "3. Testing Specific Asteroid:"
echo "URL: $BASE_URL/asteroids/2000433"
curl -s -X GET "$BASE_URL/asteroids/2000433"
echo ""
echo "----------------------------------------"
echo ""

# 4. Test with recent dates (más probable que tenga datos)
echo "4. Testing with Recent Dates:"
echo "URL: $BASE_URL/asteroids/feed?start_date=2024-12-10&end_date=2024-12-11"
curl -s -X GET "$BASE_URL/asteroids/feed?start_date=2024-12-10&end_date=2024-12-11"
echo ""
echo "----------------------------------------"
echo ""

echo "✅ All tests completed!"