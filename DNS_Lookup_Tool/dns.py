import dns.resolver

# Get user input for target domain and record types
target_domain = input("Enter target domain: ")
record_types_input = input("Enter record type(s) or press Enter for default run: ")

# Default list of record types
default_record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]

# Use user-provided input or default list
record_types = record_types_input.split() or default_record_types
print("Selected Record Types:", record_types)

# Create a DNS resolver
resolver = dns.resolver.Resolver()

# Perform DNS lookup for the specified domain and record types
for record_type in record_types:
    try:
        answers = resolver.resolve(target_domain, record_type)
        # Print the answers
        print(f"{record_type} records for {target_domain}: {', '.join(map(str, answers))}")
    except dns.resolver.NoAnswer:
        continue
