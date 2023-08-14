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
                                                            <label class="col-md-3 label-control" for="job_title">Job
                                                                Title</label>
                                                            <div class="col-md-9">
                                                                <input v-model="project.job_title" type="text"
                                                                    id="job_title" class="form-control border-primary"
                                                                    placeholder="Job title" name="job_title" required>
                                                                <span class="invalid-feedback">Job title is
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
                                                                    <option>project</option>
                                                                    <option>Academics</option>
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
                                                            <label class="col-md-3 label-control" for="company_name">Company
                                                                Name</label>
                                                            <div class="col-md-9">
                                                                <input v-model="project.company_name" type="text"
                                                                    id="company_name" class="form-control border-primary"
                                                                    placeholder="Company Name" name="company_name" required>
                                                                <span class="invalid-feedback">Company Name is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="company_url">Company
                                                                Url</label>
                                                            <div class="col-md-9">
                                                                <input v-model="project.company_url" type="text"
                                                                    id="company_url" class="form-control border-primary"
                                                                    placeholder="Company Url" name="company_url" required>
                                                                <span class="invalid-feedback">Company Url is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="row">
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control"
                                                                for="location">Location</label>
                                                            <div class="col-md-9">
                                                                <input v-model="project.location" type="text"
                                                                    id="location" class="form-control border-primary"
                                                                    placeholder="Location" name="location" required>
                                                                <span class="invalid-feedback">Location is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                
                                                <div class="row">
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control"
                                                                for="location">Description:</label>
                                                            <div class="col-md-9">
                                                                <div class="input-group">
                                                                    <input  v-model="newDescription" type="text" class="form-control border-primary" placeholder="Type and click (+) to add to list" />
                                                                    <span class="input-group-text"><button class="btn btn-sm btn-success" type="button" @click="addDescription(index)"><i class="bi bi-plus"></i></button></span>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    
                                                        <div class="col-md-6">
                                                            <div class="card mb-2">
                                                        <div v-for="(description, descriptionIndex) in project.job_descriptions"
                                                            :key="descriptionIndex" class="description-entry my-2 mx-2">
                                                            {{ description }}
                                                            <button type="button" class="btn btn-sm btn-danger"
                                                                @click="removeDescription(index, descriptionIndex)"><i class="bi bi-x"></i></button>
                                                        </div>
                                                    </div>
                                                    </div>
                                                </div>

                                                <div class="row">
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="start_date">Start
                                                                Date</label>
                                                            <div class="col-md-9">
                                                                <input v-model="project.start_date" type="date"
                                                                    id="start_date" class="form-control border-primary"
                                                                    placeholder="Start
                                                            Date" name="start_date" required>
                                                                <span class="invalid-feedback">Start
                                                                    Date is required</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="end_date">End
                                                                date</label>
                                                            <div class="col-md-9">
                                                                <input v-model="project.end_date" type="date"
                                                                    id="end_date" class="form-control border-primary"
                                                                    placeholder="End date" name="end_date" required>
                                                                <span class="invalid-feedback">End date is required</span>
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

        const addDescription = (projectIndex) => {
            if (newDescription.value.trim() !== '') {
                const projectDescriptionToAdd = projects.value[projectIndex];
                if (projectDescriptionToAdd.job_descriptions.length < 5) {
                    projectDescriptionToAdd.job_descriptions.push(newDescription.value);
                } else {
                    console.log('Errow while adding, exceeded 5');
                }

                newDescription.value = '';
            }
        };

        const removeDescription = (projectIndex, descriptionIndex) => {
            const projectDescriptionToremove = projects.value[projectIndex];
            projectDescriptionToremove.job_descriptions.splice(descriptionIndex, 1)
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
  