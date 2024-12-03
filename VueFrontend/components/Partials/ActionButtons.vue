<template>
    <div class="row">
    <div class="form-actions my-2">
      <!-- Update Button -->
      <button
        type="submit"
        class="btn btn-sm btn-warning mx-2 float-start"
        :disabled="loadingState?.updating"
        @click="onUpdateClick"
      >
        <i class="bi bi-pencil-square"></i>
        {{ loadingState?.updating ? " Updating..." : " Update" }}
      </button>
  
      <!-- Delete Button -->
      <button
        type="button"
        @click="onDeleteClick"
        class="btn btn-sm btn-danger float-end mx-2"
        :disabled="loadingState?.deleting"
      >
        <i class="bi bi-trash3"></i>
        {{ loadingState?.deleting ? " Deleting..." : " Delete" }}
      </button>
    </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, type PropType } from 'vue';
  
  interface LoadingState {
    updating: boolean;
    deleting: boolean;
  }
  
  export default defineComponent({
    name: 'ActionButtons',
    props: {
      loadingStates: {
        type: Object as PropType<Record<number, LoadingState>>,
        required: true
      },
      index: {
        type: Number,
        required: true
      },
      onUpdate: {
        type: Function as PropType<() => void>,
        required: true
      },
      onDelete: {
        type: Function as PropType<(index: number) => void>,
        required: true
      }
    },
    computed: {
      loadingState(): LoadingState {
        return this.loadingStates[this.index];
      }
    },
    methods: {
      onUpdateClick() {
        this.onUpdate();
      },
      onDeleteClick() {
        this.onDelete(this.index);
      }
    }
  });
  </script>
  
  <style scoped>
  /* Add your component-specific styles here */
  </style>
  