https://www.openra.net/

**********************ERROR *********************************

./TiberianDawnHD-release-20250303-x86_64.AppImage
Tiberian Dawn HD has encountered a fatal error.
Please refer to the crash logs and FAQ for more information.
****************************************************************

**********************************************************
****************** SOLUTION ******************************
**********************************************************
Edit the launchers 
Force a Different OpenGL Version.
Setting environment variables
This command attempts to override the OpenGL version to 3.3

--------TiberianDawnTiberianDawn Appimage --------
MESA_GL_VERSION_OVERRIDE=3.3 MESA_GLSL_VERSION_OVERRIDE=330 ./TiberianDawnHD-release-20250303-x86_64.AppImage

--------OpenRA - Tiberian Dawn flatpak --------
/usr/bin/flatpak run --branch=beta --arch=x86_64 --command=openra-cnc --file-forwarding net.openra.OpenRA @@u %U @@

-----------------OpenRA - Dune 2000 flatpak-------------------
/usr/bin/flatpak run --branch=beta --arch=x86_64 --command=openra-d2k --file-forwarding --env=MESA_GL_VERSION_OVERRIDE=3.3 --env=MESA_GLSL_VERSION_OVERRIDE=330 net.openra.OpenRA @@u %U @@

-----------------OpenRA - Red Alert flatpak--------------------
/usr/bin/flatpak run --branch=beta --arch=x86_64 --command=openra-ra --file-forwarding  --env=MESA_GL_VERSION_OVERRIDE=3.3 --env=MESA_GLSL_VERSION_OVERRIDE=330 net.openra.OpenRA @@u %U @@


***************************************************************
*************************SYSTEM********************************
****************************************************************
System:
  Kernel: 6.8.0-54-generic arch: x86_64 bits: 64 compiler: gcc v: 13.3.0
  Desktop: Cinnamon v: 6.4.8 tk: GTK v: 3.24.41 wm: Muffin dm: LightDM
    Distro: Linux Mint 22.1 Xia base: Ubuntu 24.04 noble
Machine:
  Type: Laptop System: ASUSTeK product: K52F v: 1.0 serial: <superuser required>
  Mobo: ASUSTeK model: K52F v: 1.0 serial: <superuser required> BIOS: American Megatrends
    v: K52F.205 date: 12/28/2009
Graphics:
  Device-1: Intel Core Processor Integrated Graphics vendor: ASUSTeK driver: i915 v: kernel
    arch: Gen-5.75 ports: active: VGA-1 off: LVDS-1 empty: DP-1,HDMI-A-1 bus-ID: 00:02.0
    chip-ID: 8086:0046
CHECK KERNEL****--->>>

uname -r
OUTPUT ***---->
6.8.0-54-generic


************************ LOG *************************************

./TiberianDawnHD-release-20250303-x86_64.AppImage
Tiberian Dawn HD has encountered a fatal error.
Please refer to the crash logs and FAQ for more information.

Log files are located in /home/username/.config/openra/Logs
The FAQ is available at https://wiki.openra.net/FAQ
graphics.log
ANGLE: SDL window creation failed: Could not create GLES window surface
Modern: GL context creation failed: Could not create GL context: GLXBadFBConfig
Embedded: SDL window creation failed: Could not create GLES window surface
System.InvalidOperationException: No supported OpenGL profiles were found.
   at OpenRA.Platforms.Default.Sdl2PlatformWindow..ctor(Size requestEffectiveWindowSize, WindowMode windowMode, Single scaleModifier, Int32 vertexBatchSize, Int32 indexBatchSize, Int32 videoDisplay, GLProfile requestProfile) in /home/runner/work/TiberianDawnHD/TiberianDawnHD/engine/OpenRA.Platforms.Default/Sdl2PlatformWindow.cs:line 160
   at OpenRA.Platforms.Default.DefaultPlatform.CreateWindow(Size size, WindowMode windowMode, Single scaleModifier, Int32 vertexBatchSize, Int32 indexBatchSize, Int32 videoDisplay, GLProfile profile) in /home/runner/work/TiberianDawnHD/TiberianDawnHD/engine/OpenRA.Platforms.Default/DefaultPlatform.cs:line 22
   at OpenRA.Renderer..ctor(IPlatform platform, GraphicSettings graphicSettings) in /home/runner/work/TiberianDawnHD/TiberianDawnHD/engine/OpenRA.Game/Renderer.cs:line 94
   at OpenRA.Game.Initialize(Arguments args) in /home/runner/work/TiberianDawnHD/TiberianDawnHD/engine/OpenRA.Game/Game.cs:line 372
ANGLE: SDL window creation failed: Could not create GLES window surface
Modern: GL context creation failed: Could not create GL context: GLXBadFBConfig
Embedded: SDL window creation failed: Could not create GLES window surface
System.InvalidOperationException: No supported OpenGL profiles were found.
   at OpenRA.Platforms.Default.Sdl2PlatformWindow..ctor(Size requestEffectiveWindowSize, WindowMode windowMode, Single scaleModifier, Int32 vertexBatchSize, Int32 indexBatchSize, Int32 videoDisplay, GLProfile requestProfile) in /home/runner/work/TiberianDawnHD/TiberianDawnHD/engine/OpenRA.Platforms.Default/Sdl2PlatformWindow.cs:line 160
   at OpenRA.Platforms.Default.DefaultPlatform.CreateWindow(Size size, WindowMode windowMode, Single scaleModifier, Int32 vertexBatchSize, Int32 indexBatchSize, Int32 videoDisplay, GLProfile profile) in /home/runner/work/TiberianDawnHD/TiberianDawnHD/engine/OpenRA.Platforms.Default/DefaultPlatform.cs:line 22
   at OpenRA.Renderer..ctor(IPlatform platform, GraphicSettings graphicSettings) in /home/runner/work/TiberianDawnHD/TiberianDawnHD/engine/OpenRA.Game/Renderer.cs:line 94
   at OpenRA.Game.Initialize(Arguments args) in /home/runner/work/TiberianDawnHD/TiberianDawnHD/engine/OpenRA.Game/Game.cs:line 372

*******************************************************************

******** RUN **********
sudo apt install mesa-utils
glxinfo | grep "OpenGL version"

OUTPUT *******************

mesa-utils is already the newest version (9.0.0-2).
0 upgraded, 0 newly installed, 0 to remove and 5 not upgraded.
OpenGL version string: 2.1 Mesa 24.2.8-1ubuntu1~24.04.1


******************** OPTION *****************************
**********************************************************
add a PPA (Personal Package Archive) to get the latest versions, though this comes with some risk of system instability:

sudo add-apt-repository ppa:oibaf/graphics-drivers
sudo apt update
************************************************************


**********************************************************
****************** SOLUTION ******************************
**********************************************************
Edit the launchers 
Force a Different OpenGL Version.
Setting environment variables
This command attempts to override the OpenGL version to 3.3

--------TiberianDawnTiberianDawn Appimage --------
MESA_GL_VERSION_OVERRIDE=3.3 MESA_GLSL_VERSION_OVERRIDE=330 ./TiberianDawnHD-release-20250303-x86_64.AppImage

--------OpenRA - Tiberian Dawn flatpak --------
/usr/bin/flatpak run --branch=beta --arch=x86_64 --command=openra-cnc --file-forwarding net.openra.OpenRA @@u %U @@

-----------------OpenRA - Dune 2000 flatpak-------------------
/usr/bin/flatpak run --branch=beta --arch=x86_64 --command=openra-d2k --file-forwarding --env=MESA_GL_VERSION_OVERRIDE=3.3 --env=MESA_GLSL_VERSION_OVERRIDE=330 net.openra.OpenRA @@u %U @@

-----------------OpenRA - Red Alert flatpak--------------------
/usr/bin/flatpak run --branch=beta --arch=x86_64 --command=openra-ra --file-forwarding  --env=MESA_GL_VERSION_OVERRIDE=3.3 --env=MESA_GLSL_VERSION_OVERRIDE=330 net.openra.OpenRA @@u %U @@



