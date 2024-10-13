import os

class Config:
    SECRET_KEY = os.urandom(16)
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PAILLIER_MASTER_KEY = (
        0xdd8b5a98160d7a841931f43f301bb3361911f569972e8e1781688dea4f7374628638c2c064e75c37b15541c692a7a6f8873f0e540347792a566ea348300e7a476d69f267cbe1a04852b9d3d8a4deb81cc4b84c6eb5ff123f46685bbc4c0de680f88ad5a3fa354ae6aeb3985c22bc182b7de20a78976d815b45dbccfb3fc9f6692590ba707fbdf08c6e4814a31ae994ad5142dadf274566a9296f479e766deb2d59fe3d31ed962681368a21e19505256cbf545ae74ad7dde3dace67f9576b6055bf2b99b93aaf1998cf749e8c50d6ed4a9b309ccbd26b8166e92580dda5628b6a32681919102881efe419aca4b9d067c9a3fd06d124ca899729128724c09509b0, 0x5399084e85c68419e7cdfbe0a25529dcb32c484f457b7707b5bcde770016265f56ad24ae993f25f04d8483170e02747eda86dd3526d53c64b40e28f85d49d1fb5a9f6711a7526c517e85ead7bb35821fb13d4eca9c3ffe48c97216bcf341f7c0c6bf5f3cd7212bf25bcafc34f82d346236c6b53caca5e101d5e46e1136c59c1a39b6e9f8f0d1f4391eb707618701a60a45bafda7ecf2cc2d81e9cec76684d8af548494ec1ac374c47277d247a6c63a824333a48ce6b4921a2da3753826f3eac56a0507206a1b41fb0782974141ef1940cd2dd00a25996db7fc69a3b483fbcb477959860e10a2dee21314ebc2cfa2d124b8b5e2136d97c9e44a747e0ceceed261
    )