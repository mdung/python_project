from consul import Consul
import requests
import time

# Function to register a machine learning microservice in Consul
def register_ml_service(consul, service_name, service_address, service_port):
    consul.agent.service.register(
        service_name,
        address=service_address,
        port=service_port,
        tags=["machine-learning"]
    )
    print(f"Machine learning service '{service_name}' registered successfully.")

# Function to discover available machine learning microservices from Consul
def discover_ml_services(consul):
    services = consul.agent.services()
    ml_services = [service for service in services.values() if "machine-learning" in service.get("Tags", [])]
    return ml_services

# Example function representing a machine learning microservice
def ml_service_function():
    # Replace this with your actual machine learning microservice logic
    return "Machine learning inference result"

if __name__ == "__main__":
    # Initialize Consul client
    consul = Consul()

    # Register a machine learning microservice
    service_name = "ml-service-1"
    service_address = "localhost"
    service_port = 8000
    register_ml_service(consul, service_name, service_address, service_port)

    # Discover available machine learning microservices
    available_services = discover_ml_services(consul)

    # Choose a random available machine learning microservice for demonstration
    if available_services:
        selected_service = available_services[0]
        selected_service_name = selected_service["Service"]
        selected_service_address = selected_service["Address"]
        selected_service_port = selected_service["Port"]

        print(f"Selected machine learning service: {selected_service_name} at {selected_service_address}:{selected_service_port}")

        # Replace this with actual logic to make a request to the selected machine learning service
        response = requests.get(f"http://{selected_service_address}:{selected_service_port}/")
        print(f"Response from machine learning service: {response.text}")
    else:
        print("No machine learning services found.")
