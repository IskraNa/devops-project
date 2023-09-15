# tvshows - DevOps project


Needed
- Docker
- K3d
- Python 3.10
- PostgreSQL

## Running (Normal)


## Running (Docker)

- Create a `.env` file with the environment variables `POSTGRES_USER`, `POSTGRES_PASSWORD`
- `docker-compose up`

## Running (Kubernetes)

- `k3d cluster create project -p "80:80@loadbalancer -s 1 -a 1"`
- `cd kubernetes`
- `kubectl apply -f namespace.yml -f database.yml -f job.yml -f deployment.yml -f service.yml -f ingress.yml` - the order of the manifests matters

## CD

- Argo CD
- kubectl port-forward svc/argocd-server -n argocd 8080:443
