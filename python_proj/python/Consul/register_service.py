import time
import requests
from consul import Consul

# Function to register a service in Consul
def register_service(service_name, service_host, service_port):
    consul = Consul()

    # Register the service with Consul
    consul.agent.service.register(
        service_name,
        service_id=service_name,
        address=service_host,
        port=service_port,
        tags=["ai-model"]
    )

    print(f"Service {service_name} registered with Consul")

# Function to discover a service in Consul
def discover_service(service_name):
    consul = Consul()

    # Discover services with the specified name
    services = consul.agent.services()
    instances = [service for service in services.values() if service['Service'] == service_name]

    if not instances:
        print(f"No instances of {service_name} found in Consul")
        return None

    # Select the first instance for simplicity (you can implement more advanced logic)
    instance = instances[0]

    # Return the service endpoint
    return f"{instance['Address']}:{instance['Port']}"

# Example usage
if __name__ == "__main__":
    # Replace these values with your AI model information
    model_name = "my-ai-model"
    model_host = "localhost"
    model_port = 5000

    # Register the AI model service
    register_service(model_name, model_host, model_port)

    # Sleep to allow Consul to register the service
    time.sleep(2)

    # Discover the AI model service
    endpoint = discover_service(model_name)

    if endpoint:
        print(f"Discovered AI model endpoint: {endpoint}")
        # Now you can use the endpoint for making requests to your AI model
        # For example, you can use the 'requests' library to send a sample request
        response = requests.get(f"http://{endpoint}/predict", json={"data": "your_input_data"})
        print("Response from AI model:", response.json())
