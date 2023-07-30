<template>
  <div>
    <div class="mt-2 p-6">
      <a-breadcrumb>
        <a-breadcrumb-item
          v-for="(breadcrumb, index) in breadcrumbs"
          :key="index"
        >
          <router-link v-if="breadcrumb.to" :to="breadcrumb.to">{{
            breadcrumb.title
          }}</router-link>
          <template v-else>
            {{ breadcrumb.title }}
          </template>
        </a-breadcrumb-item>
      </a-breadcrumb>
    </div>
    <div class="container mx-auto mt-4">
      <!-- Last Update Section -->
      <div class="flex items-center justify-end text-[12px] text-gray-400">
        <span class="pr-2">Last Update:</span>
        <span class="">2 min ago</span>
      </div>

      <!-- Title Section -->
      <div class="mb-8">
        <h1
          class="text-[32px] rounded-[3px] text-gray-800 hover:text-gray-600 inline-block transition duration-200 font-bold mb-0"
        >
          🌏 Vite APP
        </h1>
        <p>Unified UI for tooling</p>
      </div>

      <!-- Information Section -->
      <div class="pb-8">
        <div class="flex items-center">
          <div class="flex flex-col pr-6">
            <span class="text-gray-500 mb-1">Owner</span>
            <div class="text-gray-800 flex items-center">
              <div class="mr-1">
                <a-avatar style="background-color: #f56a00" :size="24">
                  H
                </a-avatar>
              </div>
              <span> Hasan Muzak </span>
            </div>
          </div>
          <div class="flex flex-col pr-6">
            <span class="text-gray-500 mb-1">Tags</span>
            <div>
              <span
                class="bg-sky-50 text-sky-500 text-[10px] p-1 rounded-[3px] hover:bg-sky-100"
              >
                Dashboard
              </span>
            </div>
          </div>
          <div class="flex flex-col">
            <span class="text-gray-500 mb-1">Created At</span>
            <div>
              <span> 15.07.2023 - 15:38 </span>
            </div>
          </div>
        </div>
      </div>

      <!-- Search Section -->
      <div class="mb-4 flex items-center">
        <div class="w-[230px]">
          <a-input
            v-model:value="searchKeyword"
            placeholder="Search by title..."
            size="large"
          >
            <template #suffix>
              <span>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="icon icon-tabler icon-tabler-search"
                  width="16"
                  height="16"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  fill="none"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                  <path d="M10 10m-7 0a7 7 0 1 0 14 0a7 7 0 1 0 -14 0"></path>
                  <path d="M21 21l-6 -6"></path>
                </svg>
              </span>
            </template>
          </a-input>
        </div>
        <div class="flex items-center justify-center pl-3">
          <a-avatar-group
            :max-count="2"
            :max-style="{ color: '#f56a00', backgroundColor: '#fde3cf' }"
          >
            <a-avatar
              src="https://upload.wikimedia.org/wikipedia/commons/3/33/Mark_Kassen%2C_Tony_C%C3%A1rdenas_and_Chris_Evans_%28cropped%29.jpg"
            />
            <a-avatar style="background-color: #1890ff">K</a-avatar>
            <a-tooltip title="Ant User" placement="top">
              <a-avatar style="background-color: #87d068"> U </a-avatar>
            </a-tooltip>
            <a-avatar style="background-color: #1890ff"> Y </a-avatar>
          </a-avatar-group>
        </div>
      </div>
      <GroupDraggable
        @onTaskClicked="handleTaskClicked"
        :groups="groups"
        @insertTask="handleInsertTask"
        @taskOutsideClicked="handleOutsideClicked"
      />
      <TaskInformation
        :data="clickedTaskData"
        @closed="handleInformationClose"
        :visible="taskInformationVisibility"
        @titleChanged="handleTitleChange"
      />
    </div>
  </div>
</template>

<script>
import draggable from "vuedraggable";
import TaskDraggable from "@/components/TaskDraggable.vue";
import GroupDraggable from "@/components/GroupDraggable.vue";
import TaskInformation from "@/components/TaskInformation.vue";

export default {
  components: {
    draggable,
    TaskDraggable,
    GroupDraggable,
    TaskInformation,
  },
  data() {
    return {
      groups: [
        {
          title: "Not Started",
          color: "rose",
          tasks: [
            {
              id: 1,
              group_id: 1,
              title: "Tag Refactoring",
              tags: [
                {
                  title: "sandbox",
                  color: "orange",
                },
              ],
            },
            {
              id: 2,
              group_id: 1,
              title: "Homepage Issues",
              tags: [
                {
                  title: "prod",
                  color: "sky",
                },
                {
                  title: "selenium",
                  color: "yellow",
                },
              ],
            },
            {
              id: 3,
              title: "Review User Events",
              tags: [],
            },
            {
              id: 4,
              title: "Can we create a new landing page for premium users?",
              tags: [],
            },
          ],
          id: 1,
        },
        {
          id: 2,
          title: "In Progress",
          color: "orange",
          tasks: [
            {
              id: 1,
              group_id: 2,
              title: "About Me page issues",
              tags: [],
            },
            {
              id: 2,
              group_id: 2,
              title: "Career page issues",
              tags: [],
            },
          ],
        },
        {
          id: 3,
          title: "Completed",
          color: "lime",
          tasks: [],
        },
        {
          id: 4,
          title: "Review",
          color: "indigo",
          tasks: [],
        },
      ],
      taskInformationVisibility: false,
      clickedTaskData: {},
      breadcrumbs: [
        {
          title: "Home",
          to: "/",
        },
        {
          title: "Projects",
          to: "/projects",
        },
        {
          title: "Vite App",
          to: null,
        },
      ],
      searchKeyword: "",
    };
  },
  methods: {
    modifyGroupData() {
      for (let i = 0; i < this.groups.length; i++) {
        for (let y = 0; y < this.groups[i].tasks.length; y++) {
          this.groups[i].tasks[y]["editModeEnabled"] = false;
          this.groups[i].tasks[y]["outsideClickCounter"] = 0;
        }
      }
    },
    handleTaskClicked(data) {
      if (this.taskInformationVisibility) {
        this.taskInformationVisibility = false;
      }
      this.clickedTaskData = data;
      this.taskInformationVisibility = true;
    },
    handleInformationClose() {
      this.taskInformationVisibility = false;
    },
    handleTitleChange(data) {
      console.log(data);
    },
    handleInsertTask($event) {
      const idx = this.groups.findIndex((x) => x.id === $event);

      if (idx === -1) {
        console.log("err");
        return;
      }

      const id = Math.floor(Math.random() * 1000);
      const temp = {
        id: id,
        title: "",
        tags: [],
        editModeEnabled: false,
      };

      this.groups[idx].tasks.push(temp);

      setTimeout(() => {
        const length = this.groups[idx].tasks.length;
        this.groups[idx].tasks[length - 1].editModeEnabled = true;
      }, 10);
    },
    handleOutsideClicked() {
      for (let i = 0; i < this.groups.length; i++) {
        for (let y = 0; y < this.groups[i].tasks.length; y++) {
          this.groups[i].tasks[y]["editModeEnabled"] = false;
        }
      }
    },
  },
  mounted() {
    this.modifyGroupData();
  },
};
</script>

<style lang="less" scoped>
::v-deep(.ant-breadcrumb-link) {
  font-size: 13px;
  a {
    color: #4889e5;
    transition: 0.2s;
    padding: 2px 4px;
    border-radius: 3px;
    &:hover {
      background-color: #edf1f7;
    }
  }
}
</style>
