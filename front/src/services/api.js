import config from "@/config.js";
import { v4 as uuidv4 } from "uuid";

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

export async function getContacts() {
  const settings = {
    method: "GET",
    headers: {
      Authorization: "Bearer " + getAccessToken(),
    },
  };
  const response = await fetch(`${config.API_PATH}/contacts`, settings);
  const contacts = await response.json();
  return contacts;
}

export async function getContact(id) {
  const settings = {
    method: "GET",
    headers: {
      Authorization: getUserId(),
    },
  };
  const response = await fetch(`${config.API_PATH}/contacts/${id}`, settings);
  return await response.json();
}

export async function updateContact(contact) {
  const settings = {
    method: "PUT",
    body: JSON.stringify(contact),
    headers: {
      "Content-Type": "application/json",
      Authorization: getUserId(),
    },
  };
  await fetch(`${config.API_PATH}/contacts/${contact.id}`, settings);
}

export async function addContact(contact) {
  contact.id = uuidv4();
  const settings = {
    method: "POST",
    body: JSON.stringify(contact),
    headers: {
      "Content-Type": "application/json",
      Authorization: getUserId(),
    },
  };
  await fetch(`${config.API_PATH}/contacts`, settings);
}
