curl -N -X POST  -H "Content-Type: application/json"  -H "accept: text/event-stream"  -d '{"prompt":"Streaming responseのテスト"}'  http://127.0.0.1:8000/api/llm