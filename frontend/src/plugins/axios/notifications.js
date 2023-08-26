import { notification } from "ant-design-vue";

export const showNotification = (type, description) => {
  notification[type]({
    message: "Request ERROR",
    description: description,
  });
};
