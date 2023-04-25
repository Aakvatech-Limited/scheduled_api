# Scheduled API Request Module

This module is designed to handle scheduled API requests in a Frappe application, allowing for asynchronous processing, execution outcome management, response creation, and communication with external systems via callback URLs.

## Features

1. **Asynchronous task execution**: The module utilizes Frappe's background job system to enqueue and execute tasks asynchronously.
2. **Schedule Request processing**: The module processes "Schedule Request" documents and determines whether to create a new document or call a specified method based on the request.
3. **Error handling and retries**: The module gracefully handles exceptions during request execution, updates the status accordingly, and retries failed requests.
4. **Schedule Response creation**: The module creates "Schedule Response" documents based on the outcome of the request execution, including success, errors, and traceback information.
5. **Callback URL support**: The module supports sending responses to specified callback URLs, with configurable headers and automatic retries upon failure.
6. **Pending and Failed request processing**: The module provides a function to process all pending and failed "Schedule Request" documents, allowing for easier recovery and rescheduling.
7. **Modular design**: The module is organized into separate functions for enqueueing, executing, and sending responses, which promotes readability and maintainability.

## Installation

1. Clone the repository into your Frappe application.
```
git clone <repository_url>
```

2. Install the required dependencies.

3. Configure the module in your Frappe application according to your requirements.

## Usage

- Create and configure "Schedule Request" documents with the desired method, data, and callback information.

- Use the provided functions to enqueue, execute, and manage requests and responses, as well as process all pending and failed requests.

- Monitor and manage "Schedule Response" documents for response status, data, errors, and traceback information.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue if you find a bug or would like to request a new feature.

## License

This project is licensed under the gpl3 License - see the LICENSE.txt file for details.

## Acknowledgments

- Yousef Restom
- Mitesh P Choksi
