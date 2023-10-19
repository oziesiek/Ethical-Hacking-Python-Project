import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def get_phone_number_info(phone_number):
    parsed_number = phonenumbers.parse(phone_number, None)
    
    # Get geographical information
    country = geocoder.country_name_for_number(parsed_number, "en")
    region = geocoder.description_for_number(parsed_number, "en")
    
    # Get carrier information
    carrier_name = carrier.name_for_number(parsed_number, "en")
    
    # Get time zone information
    time_zone_info = timezone.time_zones_for_number(parsed_number)
    
    # Check if the number is valid
    is_valid = phonenumbers.is_valid_number(parsed_number)
    
    # Format the number
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
    
    return country, region, carrier_name, time_zone_info, is_valid, formatted_number

# Example usage
phone_number = "+00123456789"  # Replace this with the desired phone number
country, region, carrier_name, time_zone_info, is_valid, formatted_number = get_phone_number_info(phone_number)

# Print the information
print("Country:", country)
print("Region:", region)
print("Carrier:", carrier_name)
print("Time Zone:", time_zone_info)
print("Is Valid:", is_valid)
print("Formatted Number:", formatted_number)
