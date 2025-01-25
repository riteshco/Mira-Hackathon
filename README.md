# Travel Planner Flow Overview

## Version
`0.1.0`

## Name
**Travel Planner**

## Description
Offers personalized travel destination suggestions, factoring in the user's mood, budget, location, duration, safety, and cost-effectiveness.

## Inputs
- **Mood**: Defines the user’s travel vibe (e.g., adventurous, relaxing).
- **Duration**: Specifies the number of days or weeks available for travel.
- **Location**: The user’s current city/country.
- **Budget**: The user’s expected expenditure range.
- **Transport**: Preferred mode of transport (e.g., flight, train).
- **Safety Check**: Analyzes crime rate and safety of destinations.

## Workflow Stages

### 1. **First Flow (Travel Suggestions)**
   - Suggests domestic and international travel destinations based on the user’s preferences (mood, budget, location, duration).
   - Includes key attractions, costs, and travel feasibility for each destination.

### 2. **Mid First Flow (Safety Assessment)**
   - Analyzes safety data using crime-related articles about the destinations to assess their risk level.
   - Provides safety recommendations.

### 3. **Mid Second Flow (Cost Analysis)**
   - Uses the Big Mac Index to assess cost-effectiveness of destinations.
   - Provides cost breakdown and compares it with the global average to label the destination as cost-effective, moderately priced, or expensive.

### 4. **Final Flow (Final Output)**
   - Formats all the information into a structured, user-friendly JSON format suitable for a webpage display.

## Outputs
1. **Travel Suggestions**:
   - Detailed recommendations for both domestic and international destinations, including costs, feasibility, and mood alignment.

2. **Safety Assessment**:
   - A risk-level evaluation based on crime analysis, with actionable safety recommendations.

3. **Cost Analysis**:
   - Big Mac Index comparison showing the cost-effectiveness of destinations.

## Example Output

### Domestic Destinations:
1. **Destination 1**:
   - **Why it matches**: [Explanation based on user's mood and preferences]
   - **Key Attractions**: [List of attractions]
   - **Cost Breakdown**: [Approximate costs for transport, accommodation, activities]
   - **Travel Feasibility**: [How it fits within the user’s trip duration]

2. **Destination 2**:
   - [Similar details as above]

### International Destinations:
1. **Destination A (Country)**:
   - **Big Mac Index**: [Index value]
   - **Cost-Effectiveness**: [Cost-effective, moderately priced, or expensive]
   - **Travel Feasibility**: [Feasibility based on duration and mode of transport]

### Safety Assessment:
- **Risk Level**: Moderate
- **Summary**: [Analysis of crime data and safety]
- **Recommendations**: [Tips for safe travel]

### Big Mac Index:
- Comparison of Big Mac prices between destinations.

---

This flow combines detailed user input analysis with robust external data sources (e.g., crime news and Big Mac Index) to offer a comprehensive travel plan.
