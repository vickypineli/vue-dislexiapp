import config from "@/config.js";


function getUserId() {
  const userJson = localStorage.getItem("auth");
  const user = JSON.parse(userJson);
  return user.id;
}

function getAccessToken() {
  const jwtJson = localStorage.getItem("auth");
  const jwt = JSON.parse(jwtJson);
  return jwt.access_token;
}

export async function getActivities() {
  const settings = {
    method: "GET",
    headers: {
      Authorization: "Bearer " + getAccessToken(),
    },
  };
  const response = await fetch(`${config.API_PATH}/activities`, settings);
  const activities = await response.json();
  return activities;
}

export async function getActivity(id) {
  const settings = {
    method: "GET",
    headers: {
      Authorization: getUserId(),
    },
  };
  const response = await fetch(`${config.API_PATH}/activities/${id}`, settings);
  return await response.json();
}

