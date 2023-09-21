<template>
    <div class="card border-light mb-2">
        <div class="card-content collapse show">
            <div class="card-body card-dashboard">
                <div class="row">
                    <div class="col-md-2">
                        <button class="btn btn-sm btn-outline-danger" @click="toggleSidebar">
                            <i class="bi bi-list"></i>
                        </button>
                    </div>

                    <div class="col-md-8 text-center">
                        <input type="text" class="form-control" placeholder="Search">
                    </div>

                    <div class="col-md-2 text-right">
                        <div class="dropdown">
                            <a class="dropdown-toggle" href="#" role="button" id="userDropdown" data-toggle="dropdown"
                                aria-haspopup="true" aria-expanded="false">
                                <i class="bi bi-person"></i>
                            </a>
                            <div class="dropdown-menu dropdown-menu-right" aria-labelledby="userDropdown">
                                <a class="dropdown-item" href="#"><i class="bi bi-gear"></i> Settings</a>
                                <a class="dropdown-item" href="#"><i class="bi bi-person"></i> Profile</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            sidebarOpen: true,
        };
    },
    methods: {
        toggleSidebar() {
            this.sidebarOpen = !this.sidebarOpen;
        },
    },
};
</script>

<style lang="scss" scoped>

</style>