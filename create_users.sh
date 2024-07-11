#!/bin/bash

# Nextcloud admin credentials
admin_user="admin"
admin_pass="admin123"

# Nextcloud server URL
server_url="http://localhost:8080"

# Number of users to create
num_users=30

# Loop to create users
for i in $(seq 1 $num_users)
do
  username="user$i"
  # Generate a unique password for each user
  password="Test1234_$i"

  echo "Creating user $username with password $password"

  # Create user via Nextcloud provisioning API
  response=$(curl -u "$admin_user:$admin_pass" -X POST "$server_url/ocs/v1.php/cloud/users" -d userid="$username" -d password="$password" -H "OCS-APIRequest: true")

  # Check if user creation was successful
  if echo "$response" | grep -q "<status>ok</status>"; then
    echo "User $username created successfully."
  else
    echo "Failed to create user $username."
    echo "Response: $response"
  fi
done

