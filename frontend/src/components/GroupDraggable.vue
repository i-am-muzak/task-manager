<template>
  <div>
    <!-- Group Draggable Section -->
    <div class="">
      <div class="flex items-center border-b mb-5">
        <div
          v-for="(tab, idx) in tabs"
          :key="tab.key"
          @click="handleTabChange(idx)"
        >
          <a-popover
            v-model:visible="tab.popover_visible"
            trigger="click"
            placement="bottomLeft"
            overlayClassName="custom-tab-popover"
            :align="{
              offset: [0, 10],
            }"
          >
            <template #title>
              <div class="p-1">
                <div class="">
                  <a-input
                    v-model:value="tab.title"
                    :bordered="true"
                    placeholder="Tab's name here..."
                    :maxlength="30"
                  />
                </div>
              </div>
            </template>
            <template #content>
              <div>
                <div class="p-1">
                  <div
                    class="flex items-center p-1.5 rounded hover:bg-gray-100 transition duration-200 cursor-pointer"
                  >
                    <span class="mr-1">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="icon icon-tabler icon-tabler-copy"
                        width="18"
                        height="18"
                        viewBox="0 0 24 24"
                        stroke-width="1.75"
                        stroke="currentColor"
                        fill="none"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                      >
                        <path
                          stroke="none"
                          d="M0 0h24v24H0z"
                          fill="none"
                        ></path>
                        <path
                          d="M8 8m0 2a2 2 0 0 1 2 -2h8a2 2 0 0 1 2 2v8a2 2 0 0 1 -2 2h-8a2 2 0 0 1 -2 -2z"
                        ></path>
                        <path
                          d="M16 8v-2a2 2 0 0 0 -2 -2h-8a2 2 0 0 0 -2 2v8a2 2 0 0 0 2 2h2"
                        ></path>
                      </svg>
                    </span>
                    <span class="text-[12px] font-semibold"> Duplicate </span>
                  </div>
                  <div
                    class="flex items-center p-1.5 rounded hover:bg-gray-100 transition duration-200 cursor-pointer"
                  >
                    <span class="mr-1">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="icon icon-tabler icon-tabler-trash"
                        width="18"
                        height="18"
                        viewBox="0 0 24 24"
                        stroke-width="1.75"
                        stroke="currentColor"
                        fill="none"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                      >
                        <path
                          stroke="none"
                          d="M0 0h24v24H0z"
                          fill="none"
                        ></path>
                        <path d="M4 7l16 0"></path>
                        <path d="M10 11l0 6"></path>
                        <path d="M14 11l0 6"></path>
                        <path
                          d="M5 7l1 12a2 2 0 0 0 2 2h8a2 2 0 0 0 2 -2l1 -12"
                        ></path>
                        <path
                          d="M9 7v-3a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v3"
                        ></path>
                      </svg>
                    </span>
                    <span class="text-[12px] font-semibold"> Delete </span>
                  </div>
                </div>
              </div>
            </template>
            <div
              class="flex items-center px-2 py-1 rounded-[3px] text-gray-400 cursor-pointer mr-2 mb-1 text-[12px] font-semibold custom-tab select-none"
              :class="
                activeTab === idx
                  ? 'bg-gray-200 text-gray-700 active'
                  : 'hover:bg-gray-50'
              "
            >
              <span class="mr-1">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="icon icon-tabler icon-tabler-template"
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  stroke-width="1.75"
                  stroke="currentColor"
                  fill="none"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                  <path
                    d="M4 4m0 1a1 1 0 0 1 1 -1h14a1 1 0 0 1 1 1v2a1 1 0 0 1 -1 1h-14a1 1 0 0 1 -1 -1z"
                  ></path>
                  <path
                    d="M4 12m0 1a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v6a1 1 0 0 1 -1 1h-4a1 1 0 0 1 -1 -1z"
                  ></path>
                  <path d="M14 12l6 0"></path>
                  <path d="M14 16l6 0"></path>
                  <path d="M14 20l6 0"></path>
                </svg>
              </span>
              <span>{{ tab.title }}</span>
            </div>
          </a-popover>
        </div>
      </div>
      <draggable
        class="grid lg:grid-cols-4 gap-8 md:grid-cols-3 sm:grid-cols-2 grid-cols-1"
        :list="groups"
        :group="{ name: 'groups' }"
        @start="drag = true"
        @end="drag = false"
        item-key="id"
        v-bind="dragOptions"
      >
        <template #item="{ element }">
          <div class="group-section">
            <div class="cursor-move">
              <!-- Group Header -->
              <div class="flex items-center justify-between">
                <div class="flex items-center">
                  <span
                    :class="getComputedGroupColor(element.color)"
                    class="text-[12px] font-semibold py-1 px-2 rounded-[3px] cursor-pointer select-none transition duration-200"
                  >
                    {{ element.title }}
                  </span>
                  <span class="ml-2 counter-text">
                    {{ element.tasks.length }}
                  </span>
                </div>
                <div class="flex items-center task-header-options">
                  <span
                    class="text-gray-400 hover:text-gray-700 p-1 rounded hover:bg-gray-200 cursor-pointer mr-2 flex items-center justify-center"
                  >
                    <span>
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="icon icon-tabler icon-tabler-dots"
                        width="16"
                        height="16"
                        viewBox="0 0 24 24"
                        stroke-width="1.5"
                        stroke="currentColor"
                        fill="none"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                      >
                        <path
                          stroke="none"
                          d="M0 0h24v24H0z"
                          fill="none"
                        ></path>
                        <path
                          d="M5 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0"
                        ></path>
                        <path
                          d="M12 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0"
                        ></path>
                        <path
                          d="M19 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0"
                        ></path>
                      </svg>
                    </span>
                  </span>
                  <span
                    class="text-gray-400 hover:text-gray-700 p-1 rounded hover:bg-gray-200 cursor-pointer flex items-center justify-center"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="icon icon-tabler icon-tabler-plus"
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
                      <path d="M12 5l0 14"></path>
                      <path d="M5 12l14 0"></path>
                    </svg>
                  </span>
                </div>
              </div>
              <!---- Header End ---->
            </div>
            <!-- Task Section -->
            <div class="mt-4">
              <TaskDraggable
                :tasks="element.tasks"
                @onTaskClicked="handleOnTaskClicked"
                @insertTask="handleInsertTask(element.id)"
                @outsideClicked="handleOutsideClicked"
              />
            </div>
            <!-- Task End -->
          </div>
        </template>
      </draggable>
    </div>
  </div>
</template>

<script>
import draggable from "vuedraggable";
import TaskDraggable from "@/components/TaskDraggable.vue";

export default {
  props: {
    groups: {
      type: Array,
      default: [],
    },
  },
  components: {
    draggable,
    TaskDraggable,
  },
  data() {
    return {
      drag: false,
      visible: false,
      activeTab: 1,
      tabs: [
        {
          title: "By Status",
          popover_visible: false,
          key: 1,
        },
        {
          title: "By Priority",
          popover_visible: false,
          key: 2,
        },
        {
          title: "My Tasks",
          popover_visible: false,
          key: 3,
        },
      ],
      draggable: true,
    };
  },
  methods: {
    getComputedGroupColor(color) {
      if (color) {
        const computedColor = color.toLowerCase();
        if (computedColor === "rose")
          return "bg-rose-100 text-rose-700 hover:bg-rose-50";
        if (computedColor === "orange")
          return "bg-orange-100 text-orange-700 hover:bg-orange-50";
        if (computedColor === "lime")
          return "bg-lime-100 text-lime-700 hover:bg-lime-50";
        if (computedColor === "indigo")
          return "bg-indigo-100 text-indigo-700 hover:bg-indigo-50";
        if (computedColor === "sky")
          return "bg-sky-100 text-sky-700 hover:bg-sky-50";
        if (computedColor === "blue")
          return "bg-blue-100 text-blue-700 hover:bg-blue-50";
        if (computedColor === "yellow")
          return "bg-yellow-100 text-yellow-700 hover:bg-yellow-50";
      }
      return "";
    },
    handleOnTaskClicked(task) {
      this.$emit("onTaskClicked", task);
    },
    handleActiveTabClick($event) {
      const idx = this.tabs.findIndex((x) => x.key === $event);
      if (idx === -1) {
        return;
      }
      if ($event === this.activeTab) {
        for (let i = 0; i < this.tabs.length; i++) {
          if (i === idx) {
            this.tabs[i].popover_visible = !this.tabs[i].popover_visible;
          }
        }
      } else {
        for (let i = 0; i < this.tabs.length; i++) {
          this.tabs[i].popover_visible = false;
        }
      }
    },
    handleTabChange(idx) {
      if (this.activeTab === idx) {
        // Here we can show popover.
        this.tabs[idx].popover_visible = true;
      } else {
        this.activeTab = idx;
        this.tabs[idx].popover_visible = false;
      }
    },
    handleDisableDragging() {
      this.draggable = false;
    },
    handleEnableDragging() {
      this.draggable = true;
    },
    handleInsertTask(id) {
      this.$emit("insertTask", id);
    },
    handleOutsideClicked($event) {
      this.$emit("taskOutsideClicked", $event);
    },
  },
  computed: {
    dragOptions() {
      return {
        animation: 200,
        disabled: !this.draggable,
      };
    },
  },
};
</script>

<style lang="less" scoped>
.tab-input {
  outline: none;
}

.custom-tab {
  position: relative;
}

.custom-tab.active {
  &::after {
    position: absolute;
    width: 100%;
    height: 2px;
    background-color: #374151;
    content: "";
    bottom: -5.5px;
    left: 0;
    border-radius: 3px;
  }
}

.group-section {
  .task-header-options {
    display: none;
  }

  .counter-text {
    color: rgba(55, 53, 47, 0.5);
    user-select: none;
  }

  .task-section {
    color: rgb(55, 53, 47);
    font-weight: 600;
    box-shadow: rgba(15, 15, 15, 0.1) 0px 0px 0px 1px,
      rgba(15, 15, 15, 0.1) 0px 2px 4px;
  }

  .untitled-task {
    color: rgba(55, 53, 47, 0.5);
    font-style: italic;
  }

  .task-icon {
    color: rgba(55, 53, 47, 0.85);
  }

  &:hover {
    .task-header-options {
      display: flex;
    }
  }
}
</style>
