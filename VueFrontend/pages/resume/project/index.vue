<template>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="card mb-2">
                    <div class="card-body rounded">
                        <h4 class="text-center text-uppercase bold">Project Section</h4>
                    </div>
                </div>
                <div class="card mb-2">
                    <div class="card-content collapse show">
                        <div class="card-body card-dashboard">
                            <div class="row">
                                <p class="d-inline">Project List
                                    <NuxtLink :to="'/resume/project/create'" class="btn btn-sm btn-success float-end"><i
                                            class="bi bi-plus-square"></i>{{ ' ' }}Create
                                    </NuxtLink>
                                </p>
                            </div>
                            <div v-for="(project, index) in projects" :key="index" class="card mt-2">
                                <div class="card-content collapse show">
                                    <div class="card-body card-dashboard">

                                        <div class="row">
                                            <p class="float-start"><strong>{{ index + 1 }}</strong></p>
                                        </div>
                                        
                                        <form @submit.prevent="submitProject(index)"
                                            class="form form-horizontal needs-validation" novalidate>
                                            <div class="form-body">
                                                <div class="row">
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="project_name">Project Name</label>
                                                            <div class="col-md-9">
                                                                <input v-model="project.project_name" type="text"
                                                                    id="project_name" class="form-control border-primary"
                                                                    placeholder="Project Name" name="project_name" required>
                                                                <span class="invalid-feedback">Project Name is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>

                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="card_title">Card
                                                                Title</label>
                                                            <div class="col-md-9">
                                                                <select v-model="project.card_title"
                                                                    class="form-select border-primary"
                                                                    aria-label="Default select example" required>
                                                                    <option selected :value="project.card_title">{{
                                                                        project.card_title }}</option>
                                                                    <option>Projects</option>
                                                                    <option>Personal Projects</option>
                                                                </select>
                                                                <span class="invalid-feedback">Please Select Card
                                                                    Title</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="row">
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="project_url">Project url link</label>
                                                            <div class="col-md-9">
                                                                <input v-model="project.project_url" type="text"
                                                                    id="project_url" class="form-control border-primary"
                                                                    placeholder="Project url link" name="project_url" required>
                                                                <span class="invalid-feedback">Project url link is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="project_description_title">Project Description Title</label>
                                                            <div class="col-md-9">
                                                                <input v-model="project.project_description_title" type="text"
                                                                    id="project_description_title" class="form-control border-primary"
                                                                    placeholder="Project Description Title" name="project_description_title" required>
                                                                <span class="invalid-feedback">Project Description Title is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>

                                                <div class="row">
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control"
                                                                for="location">Project Description:</label>
                                                            <div class="col-md-9">
                                                                <div class="input-group">
                                                                    <input v-model="newDescription" type="text"
                                                                        class="form-control border-primary"
                                                                        placeholder="Type and click (+) to add to list" />
                                                                    <span class="input-group-text"><button
                                                                            class="btn btn-sm btn-success" type="button"
                                                                            @click="addDescription(index)"><i
                                                                                class="bi bi-plus"></i></button></span>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>

                                                    <div class="col-md-6">
                                                        <div class="card mb-2">
                                                            <div class="card-content collapse show">
                                                                <div class="card-body card-dashboard">
                                                                    <div class="row">
                                                                        <p >Project descriptions here</p>
                                                                        <hr class="border border-primary border-2 opacity-50">
                                                                    </div>
  
                                                                    <ol type="1">
                                                                        <li v-for="(description, descriptionIndex) in project.project_description"
                                                                        :key="descriptionIndex" class="my-2 mx-2">{{ description }} <button type="button" class="btn btn-sm btn-danger"
                                                                            @click="removeDescription(index, descriptionIndex)"><i
                                                                                class="bi bi-x"></i></button></li>
                                                                    </ol>

                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="row">
                                                <div class="form-actions my-2">
                                                    <button type="submit" class="btn btn-sm btn-primary mx-2 float-start">
                                                        <i class="bi bi-pencil-square"></i>{{ ' ' }}Update
                                                    </button>

                                                    <button @click="deleteProject(project.project_id)"
                                                        class="btn btn-sm btn-danger float-end mx-2"><i
                                                            class="bi bi-trash3"></i>
                                                        {{ ' ' }}Delete
                                                    </button>
                                                </div>
                                            </div>

                                        </form>
                                        
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import { defineComponent, ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

definePageMeta({
    layout: "sidestar",
});

export default defineComponent({
    name: 'ProjectList',
    setup() {

        const projects = ref([]);
        const axios = useNuxtApp().$axios;
        const user_id = 1;
        const router = useRouter();
        const newDescription = ref('');
        
        
        const addDescription = (projectIndex) => {
            if (newDescription.value.trim() !== '') {
                const projectDescriptionToAdd = projects.value[projectIndex];
                if (projectDescriptionToAdd.project_description.length < 5) {
                    projectDescriptionToAdd.project_description.push(newDescription.value);
                }
                else {
                    console.log('Errow while adding, exceeded 5');
                }
                newDescription.value = '';
            }
        };
        const removeDescription = (projectIndex, descriptionIndex) => {
            const projectDescriptionToRemove = projects.value[projectIndex];
            projectDescriptionToRemove.project_description.splice(descriptionIndex, 1);
        };

        const getProjects = async () => {
            try {
                const response = await axios.get(`/user/${user_id}/project/`);
                projects.value = response.data;
            } catch (error) {
                console.error('Error fetching projects:', error);
            }
        };

        const updateProject = async (projectIndex) => {
            try {
                await axios.patch(
                    `/user/${projectIndex.user_id}/project/${projectIndex.project_id}`,
                    projectIndex
                ).then(function (response) {
                    console.log(response);
                    router.push('/resume/project');
                });
            } catch (error) {
                console.error('Error updating:', error);
            }
        };

        const deleteProject = async (project_id) => {
            try {
                await axios.delete(`/user/${user_id}/project/${project_id}`);
                getProjects();
            } catch (error) {
                console.error('Error deleting project:', error);
            }
        };

        const submitProject = async (projectIndex) => {
            const projectToUpdate = projects.value[projectIndex];
            const form = document.querySelector('.needs-validation');

            if (!form.checkValidity()) {
                form.classList.add('was-validated');
                return;
            }

            updateProject(projectToUpdate);
        };


        onMounted(() => {
            getProjects();
        });

        return {
            projects,
            deleteProject,
            submitProject,
            addDescription,
            newDescription,
            removeDescription,
        };
    },
});
</script>
  
<style></style>
  