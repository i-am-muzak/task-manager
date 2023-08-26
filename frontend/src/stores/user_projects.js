import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const useUserProjectStore = defineStore("userProjectStore", {
  state: () => ({
    selected_user_project_id: null,
    user_projects: [],
  }),
  getters: {
    getSelectedUserProjectID() {
      return this.selected_user_project_id;
    },
    getUserProjects() {
      return this.user_projects;
    },
  },
  actions: {
    setUserProjectID(id) {
      this.selected_user_project_id = id;
    },
    setUserProjects(data) {
      this.user_projects = data;
    },
  },
});
