docker compose -f ~/projects/link-shortener-backend/docker-compose.yml up delete_invalid_links

# crontab configuration
# * * * * * ~/projects/link-shortener-backend/run_deletion_container.sh
