<template>
    <div class="row py-3">
        <div class="col-md-12">
            <div class="card mb-2">
                <div class="card-body rounded">
                    <h4 class="text-center text-uppercase bold">Profile Section</h4>
                </div>
            </div>
            <div class="card mb-2">
                <div class="card-content collapse show">
                    <div class="card-body card-dashboard">
                        <div class="row">
                            <p class="d-inline">Create New Profile
                                <NuxtLink :to="'/resume/profile'" class="btn btn-sm btn-success float-end"><i
                                        class="bi bi-list-ol"></i>{{ ' ' }}List
                                </NuxtLink>
                            </p>
                        </div>
                        <div class="card">
                            <div class="card-body">
                                <form @submit.prevent="submitProfile" class="form form-horizontal needs-validation"
                                    novalidate>
                                    <div class="form-body">
                                        <div class="row">
                                            <div class="col-md-6">
                                                <div class="form-group row mb-2">
                                                    <label class="col-md-3 label-control" for="first_name">First
                                                        Name</label>
                                                    <div class="col-md-9">
                                                        <input v-model="newProfile.first_name" type="text" id="first_name"
                                                            class="form-control border-primary" placeholder="First Name"
                                                            name="first_name" required>
                                                        <span class="invalid-feedback">First Name is
                                                            required</span>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="form-group row mb-2">
                                                    <label class="col-md-3 label-control" for="last_name">Last
                                                        Name</label>
                                                    <div class="col-md-9">
                                                        <input v-model="newProfile.last_name" type="text" id="last_name"
                                                            class="form-control border-primary" placeholder="Last Name"
                                                            name="last_name" required>
                                                        <span class="invalid-feedback">Last Name is
                                                            required</span>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="row">
                                            <div class="col-md-6">
                                                <div class="form-group row mb-2">
                                                    <label class="col-md-3 label-control" for="middle_name">Middle
                                                        Name</label>
                                                    <div class="col-md-9">
                                                        <input v-model="newProfile.middle_name" type="text" id="middle_name"
                                                            class="form-control border-primary" placeholder="Middle Name"
                                                            name="middle_name" required>
                                                        <span class="invalid-feedback">Middle Name is
                                                            required</span>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="form-group row mb-2">
                                                    <label class="col-md-3 label-control" for="image_url">Image url
                                                        link</label>
                                                    <div class="col-md-9">
                                                        <input v-model="newProfile.image_url" type="text" id="image_url"
                                                            class="form-control border-primary" placeholder="Image url link"
                                                            name="image_url" required>
                                                        <span class="invalid-feedback">Image url link is
                                                            required</span>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <div class="row">
                                            <div class="col-md-6">
                                                <div class="form-group row mb-2">
                                                    <label class="col-md-3 label-control" for="linkedin_url">linkedIn
                                                        Url</label>
                                                    <div class="col-md-9">
                                                        <input v-model="newProfile.linkedin_url" type="text"
                                                            id="linkedin_url" class="form-control border-primary"
                                                            placeholder="linkedIn Url" name="linkedin_url" required>
                                                        <span class="invalid-feedback">linkedIn Url is
                                                            required</span>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="form-group row mb-2">
                                                    <label class="col-md-3 label-control" for="github_url">Github
                                                        url link</label>
                                                    <div class="col-md-9">
                                                        <input v-model="newProfile.github_url" type="text" id="github_url"
                                                            class="form-control border-primary"
                                                            placeholder="Github url link" name="github_url" required>
                                                        <span class="invalid-feedback">Github url link is
                                                            required</span>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <div class="row">
                                            <div class="col-md-6">
                                                <div class="form-group row mb-2">
                                                    <label class="col-md-3 label-control" for="address">Postal
                                                        Address</label>
                                                    <div class="col-md-9">
                                                        <input v-model="newProfile.address" type="text" id="address"
                                                            class="form-control border-primary" placeholder="Postal Address"
                                                            name="address" required>
                                                        <span class="invalid-feedback">Postal Address is
                                                            required</span>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="form-group row mb-2">
                                                    <label class="col-md-3 label-control" for="personal_website">Personal
                                                        Website Url</label>
                                                    <div class="col-md-9">
                                                        <input v-model="newProfile.personal_website" type="text"
                                                            id="personal_website" class="form-control border-primary"
                                                            placeholder="Personal Website Url" name="personal_website"
                                                            required>
                                                        <span class="invalid-feedback">Personal Website Url is
                                                            required</span>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <div class="row">
                                            <div class="col-md-6">
                                                <div class="form-group row mb-2">
                                                    <label class="col-md-3 label-control" for="city">City
                                                        Name</label>
                                                    <div class="col-md-9">
                                                        <input v-model="newProfile.city" type="text" id="city"
                                                            class="form-control border-primary" placeholder="City Name"
                                                            name="city" required>
                                                        <span class="invalid-feedback">City Name is
                                                            required</span>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="form-group row mb-2">
                                                    <label class="col-md-3 label-control" for="country">Country of
                                                        Residence</label>
                                                    <div class="col-md-9">
                                                        <input v-model="newProfile.country" type="text" id="country"
                                                            class="form-control border-primary"
                                                            placeholder="Country of Residence" name="country" required>
                                                        <span class="invalid-feedback">Country of Residence is
                                                            required</span>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <div class="row">
                                            <div class="col-md-6">
                                                <div class="form-group row mb-2">
                                                    <label class="col-md-3 label-control" for="user_work_title">Job
                                                        Title</label>
                                                    <div class="col-md-9">
                                                        <input v-model="newProfile.user_work_title" type="text"
                                                            id="user_work_title" class="form-control border-primary"
                                                            placeholder="Job Title" name="user_work_title" required>
                                                        <span class="invalid-feedback">Job Title is
                                                            required</span>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="form-group row mb-2">
                                                    <label class="col-md-3 label-control" for="user_summary">Job
                                                        summary</label>
                                                    <div class="col-md-9">
                                                        <input v-model="newProfile.user_summary" type="text"
                                                            id="user_summary" class="form-control border-primary"
                                                            placeholder="Job summary" name="user_summary" required>
                                                        <span class="invalid-feedback">Job summary is
                                                            required</span>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <div class="row">
                                            <div class="col-md-6">
                                                <div class="form-group row mb-2">
                                                    <label class="col-md-3 label-control" for="objectives">Job
                                                        Objective</label>
                                                    <div class="col-md-9">
                                                        <input v-model="newProfile.objectives" type="text" id="objectives"
                                                            class="form-control border-primary" placeholder="Job Objective"
                                                            name="objectives" required>
                                                        <span class="invalid-feedback">Job Objective is
                                                            required</span>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <div class="row">
                                            <div class="col-md-6">
                                                <div class="form-group row mb-2">
                                                    <label class="col-md-3 label-control" for="location">Skills:</label>
                                                    <div class="col-md-9">
                                                        <div class="input-group">
                                                            <input v-model="newSkill" type="text"
                                                                class="form-control border-primary"
                                                                placeholder="Type and click (+) to add to list" />
                                                            <span class="input-group-text"><button
                                                                    class="btn btn-sm btn-success" type="button"
                                                                    @click="addSkill"><i
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
                                                                <p>Skills here</p>
                                                                <hr class="border border-primary border-2 opacity-50">
                                                            </div>

                                                            <ol type="1">
                                                                <li v-for="(skill, skillIndex) in newProfile.skills"
                                                                    :key="skillIndex" class="my-2 mx-2">{{
                                                                        skill }} <button type="button"
                                                                        class="btn btn-sm btn-danger"
                                                                        @click="removeSkill(skillIndex)"><i
                                                                            class="bi bi-x"></i></button></li>
                                                            </ol>

                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <div class="row">
                                            <div class="col-md-6">
                                                <div class="form-group row mb-2">
                                                    <label class="col-md-3 label-control" for="location">Hobbies:</label>
                                                    <div class="col-md-9">
                                                        <div class="input-group">
                                                            <input v-model="newHobby" type="text"
                                                                class="form-control border-primary"
                                                                placeholder="Type and click (+) to add to list" />
                                                            <span class="input-group-text"><button
                                                                    class="btn btn-sm btn-success" type="button"
                                                                    @click="addHobby"><i
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
                                                                <p>Hobbies here</p>
                                                                <hr class="border border-primary border-2 opacity-50">
                                                            </div>

                                                            <ol type="1">
                                                                <li v-for="(hobby, hobbyIndex) in newProfile.hobbies"
                                                                    :key="hobbyIndex" class="my-2 mx-2">{{
                                                                        hobby }} <button type="button"
                                                                        class="btn btn-sm btn-danger"
                                                                        @click="removeHobby(hobbyIndex)"><i
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
                                            <NuxtLink :to="'/resume/profile'"
                                                class="btn btn-sm btn-danger mx-2 float-start">
                                                <i class="bi bi-x-lg"></i>{{ ' ' }}Cancel
                                            </NuxtLink>
                                            <button type="submit" class="btn btn-sm btn-primary mx-2 float-end">
                                                <i class="bi bi-check2-square"></i>{{ ' ' }}Save
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
</template>

<script>
import { defineComponent, ref } from 'vue';
import { useRouter } from 'vue-router';

export default defineComponent({
    name: 'createProfile',
    setup() {

        definePageMeta({
            layout: "sidestar",
        });

        const axios = useNuxtApp().$axios;
        const newProfile = ref({ first_name: '', last_name: '', middle_name: '', image_url: '', linkedin_url: '', github_url: '', personal_website: '', city: '', country: '', address: '', user_work_title: '', user_summary: '', objectives: '', hobbies: [], skills: [] });
        const newSkill = ref('');
        const newHobby = ref('');
        const router = useRouter();

        //Add and remove a skill
        const addSkill = () => {

            if (newSkill.value.trim() !== '') {
                const profileSkillToAdd = newProfile.value.skills;
                if (profileSkillToAdd.length < 5) {
                    profileSkillToAdd.push(newSkill.value);
                } else {
                    console.log('Errow while adding, exceeded 5');
                }

                newSkill.value = '';
            }
        };

        const removeSkill = (skillIndex) => {
            const profileSkillToRemove = newProfile.value.skills;
            profileSkillToRemove.splice(skillIndex, 1)
        };

        //add and remove a hobby
        const addHobby = () => {

            if (newHobby.value.trim() !== '') {
                const profileHobbyToAdd = newProfile.value.hobbies;
                if (profileHobbyToAdd.length < 5) {
                    profileHobbyToAdd.push(newHobby.value);
                } else {
                    console.log('Errow while adding, exceeded 5');
                }

                newHobby.value = '';
            }
        };

        const removeHobby = (hobbyIndex) => {
            const profileHobbyToRemove = newProfile.value.hobbies;
            profileHobbyToRemove.splice(hobbyIndex, 1)
        };

        const createProfile = async () => {
            const form = document.querySelector('.needs-validation');
            const user_id = 1;
            if (form.checkValidity()) {
                await axios({
                    method: 'post',
                    url: `/user/${user_id}/profile/`,
                    headers: { 'Content-Type': 'application/json' },
                    data: JSON.stringify(newProfile.value),
                })
                    .then(function (response) {
                        router.push('/resume/profile');
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
                        createProfile();
                    }
                }, false);
            });
        });

        return {
            newProfile,
            addSkill,
            newSkill,
            removeSkill,
            addHobby,
            newHobby,
            removeHobby
        };
    },
});
</script>
  
<style></style>
  