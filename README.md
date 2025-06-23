# Mistral ADK Boilerplate

This project is a boilerplate for creating an Agent Development Kit (ADK) using Mistral. It provides a base setup for developing agents with the Mistral model.

## Installation

To set up this project, follow these steps:

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. **Upgrade pip, setuptools, and wheel**:
   ```bash
   python -m pip install --upgrade pip setuptools wheel
   ```

3. **Install google-adk and its extensions**:
   ```bash
   pip install google-adk
   pip install 'google-adk[extensions]' --use-deprecated=legacy-resolver
   ```

## Usage

To use this project, navigate to the root directory and run the following command:
```bash
adk web
```

## Configuration

Ensure you have the necessary environment variables set up. Create a `.env` file in the `mistral-agent` directory with the following variables:
```env
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=your_google_api_key
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
MORALIS_API_KEY=your_moralis_api_key
```

## Agent Usage

The agent is defined in `mistral-agent/agent.py`. It uses the Mistral model and integrates with Tavily and Moralis APIs. To run the agent, ensure the environment variables are set correctly and execute the agent script:
```bash
python mistral-agent/agent.py
```

## License

This project is private and not intended for public distribution.
