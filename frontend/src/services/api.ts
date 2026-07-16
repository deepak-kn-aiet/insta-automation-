const API_BASE_URL = (import.meta as ImportMeta & { env?: { VITE_API_BASE_URL?: string } }).env?.VITE_API_BASE_URL || 'http://localhost:8000';

export async function getHealth() {
  const response = await fetch(`${API_BASE_URL}/health`);
  return response.json();
}
