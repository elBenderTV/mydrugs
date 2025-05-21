from apps.auth.services.auth_service import AuthService

def test_auth_flow():
    print("\n🔒 Probando el sistema de autenticación...")
    
    # 1. Test de encriptación
    password = "secret123"
    hashed = AuthService.hash_password(password)
    print(f"\n🔑 Contraseña original: {password}")
    print(f"🔐 Contraseña encriptada: {hashed}")
    print(f"✅ ¿Coincide la verificación?: {AuthService.verify_password(password, hashed)}")
    
    # 2. Test de JWT
    token = AuthService.create_access_token({"sub": "drogoboy"})
    print(f"\n🎟️ Token generado: {token}")

if __name__ == "__main__":
    test_auth_flow()