# Schema Documentation for all_weather_events_labeled.csv

### This file contains data related to all weather events, with corresponding labels.

Schema:

1. Event Type: One or two words describing the cause of the outage
    - Data Type: String

2. Valid Date: Date of the event
    - Data Type: String in YYYY-MM-DD format

3. Valid Time: Time of the event
    - Data Type: String in HH:MM:SS format

4. State: Comma seperated list of states affected
    - Data Type: String

5. Cities: Comma seperated list of Cities affected*
    - Data Type: String

6. Counties*: 
    - Data Type: String

7. Dirty*: Indicator of uncertainty when manually parsing
    - Data Type: boolean

6. description: json schema of the NWS events on the given date and given state
    - Data Type: json string
    
     * JSON Schema:
     * 
     * [
     *    {
     *        "event narrative": "Totals:00300.000M0.00K",
     *        "county/zone": "GARFIELD (ZONE)",
     *        "tz": "CST",
     *        "event type": "Ice Storm",
     *        "prd": "25.000M"
     *    }
     * ]
     * 
     * This JSON schema represents a single object in an array. It contains the following properties:
     * 
     * - "event narrative": A string representing the event narrative, which provides information about the event totals.
     * - "county/zone": A string representing the county or zone affected by the event.
     * - "tz": A string representing the time zone of the event.
     * - "event type": A string representing the type of event (e.g., Ice Storm).
     * - "prd": A string representing the event period.
     * 
     * Example usage:
     * 
     * [
     *    {
     *        "event narrative": "Totals:00300.000M0.00K",
     *        "county/zone": "GARFIELD (ZONE)",
     *        "tz": "CST",
     *        "event type": "Ice Storm",
     *        "prd": "25.000M"
     *    },
     *    {
     *        "event narrative": "Totals:00100.000M0.00K",
     *        "county/zone": "TULSA (ZONE)",
     *        "tz": "CST",
     *        "event type": "Snow Storm",
     *        "prd": "10.000M"
     *    }
     * ]
     * 
     

