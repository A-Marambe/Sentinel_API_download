# Sentinel_API_download
Download Sentinel images for given set of ROIs, given time frame and produce a desired band stack tiff and png for quality control
# Functionality
1. download s2 images directly from API 
2. capable of download only for given rois
3. capable of downloaded for given toi (time)
4. capable of creating a desired bandstack eg: B2,B3,B4, b8, B2,B3,B4, b8a .....etc
5. capable of generating true color png, which is usefull in quality control

# inputs
1. roi as geojson (shp will accept with minimal changes)
2. tile footprint (this can be get rid as users wish)
3.start time and end time

** for smoother operations will need better computer resources. as minimum tested on 4GB RAM/COREi3 1.7 diskspace requrements vary according to the 
