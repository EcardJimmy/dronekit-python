from dronekit import connect
vehicle = connect('tcp:127.0.0.1:5760',wait_ready=True)
print "Autopilot Firmware version: %s" % vehicle.version
print "Autopilot capabilities (supports ftp): %s" % vehicle.capabilities.ftp