from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from app.api.router import router          # uncomment when routes are ready
# from app.core.scheduler import start_scheduler  # uncomment when scheduler is ready


@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- Startup ---
    # TODO: init DB connection pool
    # TODO: load ML model into memory
    # TODO: start APScheduler jobs
    print("Starting up...")
    yield
    # --- Shutdown ---
    # TODO: close DB connections
    # TODO: stop scheduler
    print("Shutting down...")


app = FastAPI(
    title="Crypto Trading Bot",
    description="ML-powered BUY/SELL/HOLD signals for crypto",
    version="0.1.0",
    lifespan=lifespan,
)

# --- CORS ---
# Allows Next.js dev server to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Routes ---
# app.include_router(router, prefix="/api/v1")  # uncomment when routes are ready


# --- Health Check ---
@app.get("/health", tags=["Health"])
async def health():
    return {"status": "ok", "version": "0.1.0"}