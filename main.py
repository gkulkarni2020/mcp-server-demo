from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import uvicorn
from fastmcp import FastMCP
import json

greeting_server = FastMCP("GreetingServer")

@greeting_server.tool()
def say_hello(name: str = "World") -> str:
    """Say hello to someone with a personalized greeting.
    
    Args:
        name: The name of the person to greet (default: "World")
    
    Returns:
        A personalized greeting message
    """
    print(f"Hello, {name}! Welcome to our FastAPI MCP demo!")
    return f"Hello, {name}! Welcome to our FastAPI MCP demo!"

@greeting_server.tool()
def get_greeting_languages() -> List[str]:
    """Get a list of available greeting languages.
    
    Returns:
        List of language codes for available greetings
    """
    print(["en", "es", "fr", "de", "it", "pt", "ja", "ko", "zh"])
    return ["en", "es", "fr", "de", "it", "pt", "ja", "ko", "zh"]

@greeting_server.tool()
def multilingual_hello(name: str = "World", language: str = "en") -> str:
    """Say hello in different languages.
    
    Args:
        name: The name of the person to greet
        language: Language code (en, es, fr, de, it, pt, ja, ko, zh)
    
    Returns:
        A greeting in the specified language
    """
    greetings = {
        "en": f"Hello, {name}!",
        "es": f"¡Hola, {name}!",
        "fr": f"Bonjour, {name}!",
        "de": f"Hallo, {name}!",
        "it": f"Ciao, {name}!",
        "pt": f"Olá, {name}!",
        "ja": f"こんにちは, {name}!",
        "ko": f"안녕하세요, {name}!",
        "zh": f"你好, {name}!"
    }
    print(greetings.get(language.lower(), f"Hello, {name}!"))
    return greetings.get(language.lower(), f"Hello, {name}!")

app = greeting_server.streamable_http_app()
