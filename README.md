# Instagram Automation Assistant

A modular, production-ready personal Instagram automation assistant scaffold for one Instagram Professional account.

## Overview

This project provides a Day 1 scaffold for a full-stack application that will eventually support:

- Instagram DM and comment handling
- Keyword-based and AI-assisted replies
- Media and link sending
- Conversation history
- Analytics and automation management

## Project Structure

- backend/: FastAPI application
- frontend/: React + Vite + TypeScript + Tailwind UI
- docker/: containerization assets
- docs/: product documentation
- media/: static assets and future screenshots
- scripts/: operational scripts

## Getting Started

1. Copy .env.example to .env and adjust values.
2. Start services with Docker Compose.
3. Open the frontend and backend applications locally.

## TODO

- Implement Meta Graph API webhook ingestion.
- Add authentication and account ownership checks.
- Build persistence for conversations and automations.
- Connect AI providers (Ollama/Gemini) behind feature flags.
