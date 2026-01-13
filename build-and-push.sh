#!/bin/bash
# بناء وتشغيل BioShield على Kubernetes

# المتغيرات
IMAGE_NAME="bioshield"
TAG="3.3.0"
REGISTRY="your-registry"  # تغيير هذا

echo "🔨 بناء Docker image..."
docker build -t ${IMAGE_NAME}:${TAG} -t ${IMAGE_NAME}:latest .

echo "🏷️ tagging image..."
docker tag ${IMAGE_NAME}:${TAG} ${REGISTRY}/${IMAGE_NAME}:${TAG}
docker tag ${IMAGE_NAME}:latest ${REGISTRY}/${IMAGE_NAME}:latest

echo "📤 رفع image إلى registry..."
docker push ${REGISTRY}/${IMAGE_NAME}:${TAG}
docker push ${REGISTRY}/${IMAGE_NAME}:latest

echo "🚀 تطبيق Kubernetes manifests..."
kubectl apply -f k8s/

echo "✅ تم النشر!"
echo ""
echo "📊 التحقق من النشر:"
echo "kubectl get pods -l app=bioshield"
echo "kubectl get svc bioshield-service"
