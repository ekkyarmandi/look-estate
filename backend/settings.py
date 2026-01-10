from decouple import config


# CORS
cors = dict(
    allow_origins=config("ALLOWED_ORIGIN"),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
