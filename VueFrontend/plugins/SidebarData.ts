import Grid from '../assets/userNavigation/icons/grid.svg'
import Courses from '../assets/userNavigation/icons/courses.png'
import Profile from '../assets/userNavigation/icons/user.svg'
import Graduation_Cap from '../assets/userNavigation/icons/graduation-cap.png'
import Settings from '../assets/userNavigation/icons/settings.svg'
import Fees from '../assets/userNavigation/icons/tuition-fees.png'
import Photo from '../assets/userNavigation/icons/rony.jpg'

export default defineNuxtPlugin( () => {

   const SidebarData = [
    {
      title: "Dashboard",
      path: "/resume/start",
      icon: Grid,
      className: "dashboard-link",
    },
    {
      title: "Education",
      path: "/resume/education",
      icon: Courses,
      className: "courses-link",
    },
    {
      title: "Experience",
      path: "/resume/experience",
      icon: Fees,
      className: "fees-link",
    },
    {
      title: "Language",
      path: "/resume/language",
      icon: Fees,
      className: "fees-link",
    },
    {
      title: "Certification",
      path: "/resume/certification",
      icon: Graduation_Cap,
      className: "certificate-link",
    },
    {
      title: "Profile",
      path: "/dashboard/profile",
      icon: Profile,
      className: "profile-link",
    },
    {
      title: "Projects",
      path: "/resume/projecte",
      icon: Profile,
      className: "profile-link",
    },
    {
      title: "Referees",
      path: "/resume/referee",
      icon: Fees,
      className: "fees-link",
    },
    {
      title: "Preview",
      path: "/template",
      icon: Settings,
      className: "settings-link",
    },
    {
      title: "Settings",
      path: "/dashboard/settings",
      icon: Settings,
      className: "settings-link",
    }
  ];
  
   const userData = [
    {
      icon: Photo,
      className: "user-data",
      userName: "Ronald Kimeli",
      course: "computer Science"
    }
  ];
      return {
        provide: {
          sidebardata: SidebarData,
          userdata: userData
        }
      }
  })

