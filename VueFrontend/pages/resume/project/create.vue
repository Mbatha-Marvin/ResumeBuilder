<template>
    <div class="row py-4 px-2">
        <div class="col-xl-12 col-lg-12 col-md-12">
            <div class="card mb-2">
                <div class="card-body rounded">
                    <h4 class="text-center text-uppercase bold">Project Section</h4>
                </div>
            </div>
            <div class="card mb-2">
                <div class="card-content collapse show">
                    <div class="card-body card-dashboard">
                        <div class="row">
                            <p class="d-inline">Create New Project
                                <NuxtLink :to="'/resume/project'" class="btn btn-sm btn-success float-end"><i
                                        class="bi bi-list-ol"></i>{{ ' ' }}List
                                </NuxtLink>
                            </p>
                        </div>
                        <div class="card">
                            <div class="card-body">
                                <form @submit.prevent="createProject" class="form form-horizontal needs-validation"
                                    novalidate>
                                    <div class="form-body">
                                        <div class="row">
                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="project_name">Project
                                                        Name</label>
                                                    <input v-model="newProject.project_name" type="text"
                                                        id="project_name" class="form-control border-primary"
                                                        placeholder="Project Name" name="project_name" required>
                                                    <span class="invalid-feedback">Project Name is
                                                        required</span>
                                                </div>
                                            </div>

                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="card_title">Card
                                                        Title</label>
                                                    <select v-model="newProject.card_title"
                                                        class="form-select border-primary"
                                                        aria-label="Default select example" required>
                                                        <option disabled value="">Please Select</option>
                                                        <option>Projects</option>
                                                        <option>Personal Projects</option>
                                                    </select>
                                                    <span class="invalid-feedback">Please Select Card
                                                        Title</span>
                                                </div>
                                            </div>

                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="project_url">Project url
                                                        link</label>
                                                    <input v-model="newProject.project_url" type="text" id="project_url"
                                                        class="form-control border-primary"
                                                        placeholder="Project url link" name="project_url" required>
                                                    <span class="invalid-feedback">Project url link is
                                                        required</span>
                                                </div>
                                            </div>
                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="project_description_title">Project
                                                        Description Title</label>
                                                    <input v-model="newProject.project_description_title" type="text"
                                                        id="project_description_title"
                                                        class="form-control border-primary"
                                                        placeholder="Project Description Title"
                                                        name="project_description_title" required>
                                                    <span class="invalid-feedback">Project Description Title is
                                                        required</span>
                                                </div>
                                            </div>

                                            <div class="col-md-4">
                                                <div class="form-group mb-2">
                                                    <label class="label-control" for="location">Project
                                                        Description:</label>
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

                                                <div v-if="newProject.project_description.length > 0" class="card mb-2">
                                                    <div class="card-content collapse show">
                                                        <div class="card-body card-dashboard">
                                                            <div class="row">
                                                                <p>Project descriptions here</p>
                                                                <hr class="border border-primary border-1 opacity-50">
                                                            </div>

                                                            <ol type="1">
                                                                <li v-for="(description, projectIndex) in newProject.project_description"
                                                                    :key="projectIndex" class="my-1">{{ description }}
                                                                    <i @click="removeDescription(projectIndex)"
                                                                        class="bi bi-x bg-danger text-white"></i>
                                                                </li>
                                                            </ol>

                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <div class="row">
                                            <div class="form-actions my-2">
                                                <NuxtLink :to="'/resume/project'"
                                                    class="btn btn-sm btn-danger mx-2 float-start">
                                                    <i class="bi bi-x-lg"></i>{{ ' ' }}Cancel
                                                </NuxtLink>
                                                <button type="submit" class="btn btn-sm btn-success mx-2 float-end">
                                                    <i class="bi bi-check2-square"></i>{{ ' ' }}Save
                                                </button>

                                            </div>
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
</template>

<script>
import { defineComponent, ref } from 'vue';
import { useRouter } from 'vue-router';

export default defineComponent({
    name: 'createProject',
    setup() {

        definePageMeta({
            layout: "sidestar",
        });


        const axios = useNuxtApp().$axios;
        const newProject = ref({ card_title: '', project_name: '', project_description_title: '', project_url: '', project_description: [] });
        const newDescription = ref('');
        const router = useRouter();

        const addDescription = () => {

            if (newDescription.value.trim() !== '') {
                const projectDescriptionToAdd = newProject.value.project_description;
                if (projectDescriptionToAdd.length < 5) {
                    projectDescriptionToAdd.push(newDescription.value);
                } else {
                    console.log('Errow while adding, exceeded 5');
                }

                newDescription.value = '';
            }
        };

        const removeDescription = (projectIndex) => {
            const projectDescriptionToRemove = newProject.value.project_description;
            projectDescriptionToRemove.splice(projectIndex, 1)
        };

        const createProject = async () => {
            const form = document.querySelector('.needs-validation');
            const user_id = 1;
            if (form.checkValidity()) {
                await axios({
                    method: 'post',
                    url: `/user/${user_id}/project/`,
                    headers: { 'Content-Type': 'application/json' },
                    data: JSON.stringify(newProject.value),
                })
                    .then(function (response) {
                        router.push('/resume/project');
                        // console.log(response);
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            } else {
                form.classList.add('was-validated');
            };
        };

        onMounted(() => {
            const forms = document.querySelectorAll('.needs-validation');

            Array.from(forms).forEach(form => {
                form.addEventListener('submit', event => {
                    event.preventDefault();
                    event.stopPropagation();

                    if (!form.checkValidity()) {
                        form.classList.add('was-validated');
                    } else {
                        createProject();
                    }
                }, false);
            });
        });

        return {
            newProject,
            addDescription,
            newDescription,
            removeDescription
        };
    },
});
</script>

<style></style>