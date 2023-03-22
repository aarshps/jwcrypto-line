import jwt
from jwt.algorithms import RSAAlgorithm
import time

privateKey = {
  "alg": "RS256",
  "d": "CyyVIjyO4tbqTwKP08caVfJYdHjOh4SClDYAvAA-HoAStXRxAKzVI2a7ypiteTGqJP8-6s7t4XsYmSNvyR9zDTpQ37A-a23xWoXDghPUEJffwmKs3k4WtKusLUkNk9lzJQ_3QGTvEvCkoUyfMWliUAiiyTUo5hB1JqvT_YzMqlK9UN9GJEHYIpX6I0tmhNQY6DBEhHnjaBNvRnhZ_nuUdi3yL8lNMkvcuvWlddVxneGS7kMa53lspZs4wHkIET-28zLwERa8jDwY-WAfpuZcY9bOxIq9IOiIS-ZSEvDkHgcei6p0g51WUNIHc4pvFKZ6_o3zHnA5wwqk6p1JK7iocw",
  "dp": "YupG3OWl-IfdC1rLp12wMXjqM0sbdhgfLg1mhkP3j0D-1oPzy7yjKhE6r1f0gLhlQ8KDc-WAmjMAmaSbaTmmZKv9dqOhsS2n-uFNK3ldPmSNxwBiZGcAbgtnF4-VB1cpq3mObUV-_KqVJgWbM5DCsFvJZT3rNNleK3NQs-rkb9k",
  "dq": "53uUyg-uzfkLdAyZlKwfJkE6Azpw18mlJCEDyYTvkCAxQ5ZtCoLNgktvJlV3h5xMsiqtmRK7aOVCS_UK_NUVXWdU_BDN9ue8mULLgp3L8OHWrvfCfJkYmkFgFEElNSFLiAabjHmDeGhSNxhz39LJ5nnSGMmPCfGHmZuqkGD0rrs",
  "e": "AQAB",
  "kty": "RSA",
  "n": "zvoyonXZZE3jOMzrIFljq8f6m8XNsHY7siQf7rStH8oQMn1fxM14sOuGlwlTnqVUNRyiRP2Hj3zy4n6EbIYPaYGnRTcIbgELpX5qnS1KsAhSdDUmdGPfiz-NRJJpAKQfSz5zuElgZwLsYDmIZsjDEnVkpRuJ0Gq8zf1rRJBvEnNLzaagAU6xs_jtIqS46C3i3SlzStBWNSdUFOTkp0netQ0Izw1G3HEiUhIERU82Bld9zNBb3TjmrpEW0p5Y3pLTuwjLXqGn02cPt2XCgNT0CLRBQgzOEcijXSNPFW_qGNtab2qr1ooM3T2jEyIp8TM5FW5xrFrehSe8tqFaEuLO7Q",
  "p": "3_CFooL6pHgJgjWeLN2l7lKqZbYOy_8ymo2bN5gflPbAJWEfFz6RBWFa83c1UHKp-OxcT72tt8xzJbgYLS6DXQTLWgkzOneS113q9Z9dfaDPiLQQmOXUrSc0RfUlPTLFMl2LigccxysQ4O5J3uzY7AAWFROi67NWG2R2fs-3yn8",
  "q": "7JwA_yrba-byj5oIbf9qli7V3_TWMX7W_4BkmB_yKFVSUxpTjhRjBfsYQTYUoW6kmNJ2WcPlU8gRKFHUhufZVCILFt2H-GODGKkWAmiorahbxX4jo-kidVp2xfyo8sAPPc2215H2AICTT_bok2_m_qlNAG0EGThc9m0zeFeSeJM",
  "qi": "Z6C-lRAOQrlyd0AphXdsECfO0joIQRk0Lfa-qCtztB944AMD0o9NlzBK1jnbuQsZayfxk0ngocBHKkM-0HCnGeQ3kN6x4KsuU8V_2rLPugqD6cnlGVJXzxaCcyCNHrtdvnp5n1KS_JTcMEW3ek8ff2669q6Oo3CFpTIUBJrb8vY",
  "use": "sig"
}

headers = {
    "alg": "RS256",
    "typ": "JWT",
    "kid": "516821e8-859b-4f7e-943b-63e8755c25e9"
}

payload = {
  "iss": "1234567890",
  "sub": "1234567890",
  "aud": "https://api.line.me/",
  "exp":int(time.time())+(60 * 30),
  "token_exp": 60 * 60 * 24 * 30
}

key = RSAAlgorithm.from_jwk(privateKey)

JWT = jwt.encode(payload, key, algorithm="RS256", headers=headers, json_encoder=None)
print(JWT)