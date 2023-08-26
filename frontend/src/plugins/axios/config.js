import axios from "axios";
import Cookies from "js-cookie";
import { showNotification } from "./notifications";

const apiURL = import.meta.env.VITE_API_URL;

const authToken = Cookies.get("session_id");

const baseAxios = axios.create({
  baseURL: apiURL,
  headers: {
    "Content-Type": "application/json",
  },
});

if (authToken) {
  baseAxios.defaults.headers.authorization = `Bearer ${authToken}`;
}

baseAxios.interceptors.response.use(
  (response) => response,
  (error) => {
    // if (error.response.status === 401) {
    //   router.push({
    //     name: "login",
    //   });
    // }

    if (error.response.status >= 400 && error.response.status <= 499) {
      var errorMessage = null;
      if (error.response.data && error.response.data.detail) {
        errorMessage = error.response.data.detail;
        if (error.response.status === 422) {
          errorMessage =
            "An error occured while sending request from the web server.";
        }
      } else {
        errorMessage = error.message;
      }
      if (errorMessage) {
        showNotification("error", errorMessage);
      }
    }
    return Promise.reject(error);
  }
);

export default baseAxios;
