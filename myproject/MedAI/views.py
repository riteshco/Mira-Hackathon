from django.shortcuts import render
from django.http import HttpResponse
from mira_sdk import MiraClient
from mira_sdk.exceptions import FlowError
import os
import requests
# Create your views here.

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def head(request):
    result=0
    if request.method == "POST":
        # Get data from the form
        mood = request.POST.get("mood")
        duration = request.POST.get("duration")  
        place = request.POST.get("place")  
        budget = request.POST.get("budget")  
        mode = request.POST.get("mode")  
    
        print(mood)
        def get_crime_news(city_name, api_key):
            url = f"https://newsapi.org/v2/everything?q=crime+in+{city_name}&apiKey={api_key}"
            response = requests.get(url)
            news_data = response.json()
            return news_data
        
        news_json = get_crime_news(place, "c2c017870bfc4987ac8054dc90857069")

        client = MiraClient(config={"API_KEY": "sb-02d82ef8a1525628c728464d3cb14d4f"})
        flow_name = "riteshco/travel-planner-3"                 # Flow identifier
        input_data = {                                              # Prepare test inputs
                    "prime_input_1": mood,
                    "prime_input_2": duration,
                    "prime_input_3": place,
                    "prime_input_4": budget,
                    "prime_input_5": mode,
                    "prime_input_6": news_json,
                }
        try:
            result = client.flow.execute(flow_name, input_data)    # Execute workflow
            print("Execution result:", result)                     # Display result
        except FlowError as e:
            print("Execution error:", str(e)) 

        indexes = [i for i, char in enumerate(result) if char == '`']
        if result==0:
            result = { "Places": [
    {
      "Name": "Rishikesh, Uttarakhand",
      "Key_Attractions": [
        "Rafting in the Ganges",
        "Bungee jumping",
        "Trekking to Neergarh Waterfall",
        "Visit to Beatles Ashram"
      ],
      "Tourist_Spots": [
        "Laxman Jhula",
        "Parmarth Niketan",
        "Triveni Ghat",
        "Ram Jhula"
      ],
      "Cost_Breakdown": {
        "Transport": "$40–$60 by train/bus from Delhi",
        "Accommodation": "$20–$50 per night",
        "Activities": "$100"
      },
      "Travel_Feasibility": "Rishikesh is perfect for a 6-day trip, being just a few hours away from Delhi.",
      "Budget_Suggestions": "Stay in budget hostels and enjoy affordable rafting experiences."
    },
    {
      "Name": "Manali, Himachal Pradesh",
      "Key_Attractions": [
        "Solang Valley for paragliding",
        "Rohtang Pass for snow activities",
        "Trekking trails like Beas Kund"
      ],
      "Tourist_Spots": [
        "Hidimba Devi Temple",
        "Manu Temple",
        "Vashisht Hot Water Springs",
        "Old Manali"
      ],
      "Cost_Breakdown": {
        "Transport": "$60–$100 via bus",
        "Accommodation": "$30–$70 per night",
        "Activities": "$150–$200"
      },
      "Travel_Feasibility": "Manali is accessible for a week-long trip, maximizing outdoor fun.",
      "Budget_Suggestions": "Consider shared trips for activities to save money."
    },
    {
      "Name": "Coorg, Karnataka",
      "Key_Attractions": [
        "Abbey Falls",
        "Dubare Elephant Camp",
        "Trekking at Tadiandamol Peak"
      ],
      "Tourist_Spots": [
        "Raja's Seat",
        "Madikeri Fort",
        "Nagarhole National Park",
        "Golden Temple (Namdroling Monastery)"
      ],
      "Cost_Breakdown": {
        "Transport": "$100–$150 by flight/train and bus",
        "Accommodation": "$30–$60 per night",
        "Activities": "$100"
      },
      "Travel_Feasibility": "Coorg provides a relaxing yet adventurous getaway within 6 days.",
      "Budget_Suggestions": "Opt for homestays for a more budget-friendly experience."
    },
    {
      "Name": "Kathmandu, Nepal",
      "Key_Attractions": [
        "Boudhanath Stupa",
        "Swayambhunath Temple",
        "Short treks in the Himalayas"
      ],
      "Tourist_Spots": [
        "Pashupatinath Temple",
        "Durbar Square",
        "Patan Museum",
        "Garden of Dreams"
      ],
      "Cost_Breakdown": {
        "Transport": "$150–$200 for round-trip flights",
        "Accommodation": "$20–$50 per night",
        "Activities": "$150"
      },
      "Travel_Feasibility": "Convenient for a 6-day itinerary with a blend of culture and adventure.",
      "Budget_Suggestions": "Use local transport to explore and save on costs."
    },
    {
      "Name": "Dubai, UAE",
      "Key_Attractions": [
        "Burj Khalifa",
        "Desert safari",
        "Skydiving over Palm Jumeirah"
      ],
      "Tourist_Spots": [
        "Dubai Mall",
        "Dubai Marina",
        "Jumeirah Beach",
        "Palm Jumeirah"
      ],
      "Cost_Breakdown": {
        "Transport": "$250–$350 for flights",
        "Accommodation": "$40–$80 per night",
        "Activities": "$200"
      },
      "Travel_Feasibility": "Quick 3–4-hour flight with plenty to do in 6 days.",
      "Budget_Suggestions": "Book activities in advance for potential discounts."
    },
    {
      "Name": "Bangkok and Surroundings, Thailand",
      "Key_Attractions": [
        "Floating markets",
        "Ayutthaya Island excursions",
        "Adventure parks"
      ],
      "Tourist_Spots": [
        "Grand Palace",
        "Wat Pho",
        "Chatuchak Market",
        "Chao Phraya River"
      ],
      "Cost_Breakdown": {
        "Transport": "$300–$400 for flights",
        "Accommodation": "$30–$60 per night",
        "Activities": "$200"
      },
      "Travel_Feasibility": "Provides diverse activities suitable for 6 days of exploration.",
      "Budget_Suggestions": "Consider street food and local eateries for affordable meals."
    }
  ],
  "Safety_Assessment": {
    "Risk_Level": "Moderately Safe to Unsafe",
    "Assessment_Summary": "The presence of serious crimes such as robbery and assault within a short period could indicate potential safety concerns.",
    "Recommendations": [
      "Avoid high-risk areas and times.",
      "Stay informed through local news.",
      "Maintain vigilance and secure personal belongings.",
      "Seek safe accommodations in well-reviewed areas."
    ]
  },
  "Big_Mac_Index": [
    {
      "Place_Name": "Rishikesh, Uttarakhand",
      "Index_Value": "$2.50",
      "Global_Average_Comparison": "49% below the global average of $4.90",
      "Cost_Effectiveness_Label": "Cost-effective"
    },
    {
      "Place_Name": "Manali, Himachal Pradesh",
      "Index_Value": "$2.50",
      "Global_Average_Comparison": "49% below the global average",
      "Cost_Effectiveness_Label": "Cost-effective"
    },
    {
      "Place_Name": "Coorg, Karnataka",
      "Index_Value": "$2.50",
      "Global_Average_Comparison": "49% below the global average",
      "Cost_Effectiveness_Label": "Cost-effective"
    },
    {
      "Place_Name": "Kathmandu, Nepal",
      "Index_Value": "Data Unavailable",
      "Global_Average_Comparison": "N/A",
      "Cost_Effectiveness_Label": "N/A"
    },
    {
      "Place_Name": "Dubai, UAE",
      "Index_Value": "$6.16",
      "Global_Average_Comparison": "26% above the global average of $4.90",
      "Cost_Effectiveness_Label": "Expensive"
    },
    {
      "Place_Name": "Bangkok, Thailand",
      "Index_Value": "$3.20",
      "Global_Average_Comparison": "35% below the global average",
      "Cost_Effectiveness_Label": "Cost-effective"
    }
  ] }
        try:
            # Your existing logic to populate `result` and `indexes`
            # Ensure `indexes` is generated before the following lines
        
            if len(indexes) < 4:
                raise ValueError("Indexes list does not contain enough elements.")
        
            result = result[indexes[2] + 5 : indexes[3]]
        # Further processing of `result`
        except IndexError:
            # Handle specific index errors gracefully
            return ({"success": False, "error": "Index out of range while slicing results."})
        except Exception as e:
            # Log and handle unexpected errors
            return ({"success": False, "error": str(e)})
    return render(request, 'head.html' , {'result' : result})

# def data(request):
#     def fetch_data(request):
#     # Define the API endpoint
#         api_url = "http://127.0.0.1:8000/head"  # Replace with your API URL

#     # Send GET request to the API
#         response = requests.get(api_url)

#     # Check if the request was successful
#         if response.status_code == 200:
#         # Parse the JSON data from the response
#             result = response.json()
#         else:
#         # Handle errors (e.g., API not available, wrong endpoint, etc.)
#             result = {"error": "Failed to fetch data from API"}

#     fetch_data(request)
