<template>
  <div class="container mx-auto">
    <a-select
      placeholder="Choose a project"
      class="w-full"
      v-model:value="selected_project_id"
      :loading="loading"
      :disabled="loading"
    >
      <a-select-option
        :value="project.id"
        v-for="project in getUserProjects"
        :key="project.id"
        >{{ project.title }}
      </a-select-option>
    </a-select>
  </div>
  <RouterView />
</template>

<script>
import { mapActions, mapState } from "pinia";
import { useUserProjectStore } from "./stores/user_projects";

export default {
  data() {
    return {
      selected_project_id: null,
      loading: false,
    };
  },
  methods: {
    ...mapActions(useUserProjectStore, ["setUserProjectID", "setUserProjects"]),

    async fetchUserProjects() {
      try {
        this.loading = true;
        const request = await this.$axios.get("user-projects/all");
        this.setUserProjects(request.data);

        if (this.computedSelectedProjectFromStorage) {
          this.selected_project_id = parseInt(
            this.computedSelectedProjectFromStorage
          );

          this.setUserProjectID(
            parseInt(this.computedSelectedProjectFromStorage)
          );
        }
      } catch (error) {
        console.log(error);
      } finally {
        this.loading = false;
      }
    },

    setSelectedProjectIntoStorage() {
      if (this.selected_project_id) {
        localStorage.setItem("selectedProjectId", this.selected_project_id);
      }
    },
  },
  computed: {
    ...mapState(useUserProjectStore, ["getUserProjects"]),
    computedSelectedProjectFromStorage() {
      const selectedProject = localStorage.getItem("selectedProjectId");
      return selectedProject;
    },
  },
  watch: {
    selected_project_id() {
      this.setSelectedProjectIntoStorage();
    },
  },
  mounted() {
    this.fetchUserProjects();
  },
};
</script>
