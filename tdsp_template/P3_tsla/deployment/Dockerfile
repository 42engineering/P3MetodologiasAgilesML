# Imagen base
FROM python:3.10.12

# Directorio de trabajo
WORKDIR /app

# Copiar archivo de configuración del proyecto
COPY pyproject.toml .

# Copiar el resto del proyecto
COPY . .

# Instalar dependencias desde pyproject.toml
RUN pip install --no-cache-dir -e .

# Exponer puerto
EXPOSE 8080

# Ejecutar aplicación
CMD ["python", "app.py"]