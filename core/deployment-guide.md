1. Test Django
```
python manage.py test
```

2. Build container
```
    -t registry.digitalocean.com/<your-registry>/django-portfolio:latest \
    -t registry.digitalocean.com/<your-registry>/django-portfolio:v1
    .
```

3. Push to container registry
```
docker push registry.digitalocean.com/<your-registry>/django-portfolio --all-tags
```

4. Update Secrets
```
kubectl delete secret django-core-env
kubectl create secret django-core-env --from-end-file=web/.env.prod
```

5. Update Deployment
```
kubectl apply -f k8s/apps/portfolio-core.yaml
```

6. Wait for rollout
```
kubectl rollout status deployment/django-core-deployment
```

7. Export for Migrate
```
export SINGLE_POD_NAME=$(kubectl get pod -l app=django-core-deployment -o NAME | tail -n 1)

```

8. Run
```
kubectl exec -it $SINGLE_POD_NAME -- bash /app/migrate.sh
```
