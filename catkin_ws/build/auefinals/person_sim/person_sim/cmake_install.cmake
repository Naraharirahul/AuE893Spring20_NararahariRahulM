# Install script for directory: /home/nmalaya/folders/AuE893Spring20_NararahariRahulM/catkin_ws/src/auefinals/person_sim/person_sim

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/nmalaya/folders/AuE893Spring20_NararahariRahulM/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/nmalaya/folders/AuE893Spring20_NararahariRahulM/catkin_ws/build/auefinals/person_sim/person_sim/catkin_generated/installspace/person_sim.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/person_sim/cmake" TYPE FILE FILES
    "/home/nmalaya/folders/AuE893Spring20_NararahariRahulM/catkin_ws/build/auefinals/person_sim/person_sim/catkin_generated/installspace/person_simConfig.cmake"
    "/home/nmalaya/folders/AuE893Spring20_NararahariRahulM/catkin_ws/build/auefinals/person_sim/person_sim/catkin_generated/installspace/person_simConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/person_sim" TYPE FILE FILES "/home/nmalaya/folders/AuE893Spring20_NararahariRahulM/catkin_ws/src/auefinals/person_sim/person_sim/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/person_sim" TYPE DIRECTORY FILES
    "/home/nmalaya/folders/AuE893Spring20_NararahariRahulM/catkin_ws/src/auefinals/person_sim/person_sim/launch"
    "/home/nmalaya/folders/AuE893Spring20_NararahariRahulM/catkin_ws/src/auefinals/person_sim/person_sim/models"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/person_sim" TYPE DIRECTORY FILES "/home/nmalaya/folders/AuE893Spring20_NararahariRahulM/catkin_ws/src/auefinals/person_sim/person_sim/scripts" USE_SOURCE_PERMISSIONS)
endif()

