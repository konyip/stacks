###################################################################################################
#
# Source and include definition
#
# Copyright (c) 2013-2018 Arm Ltd.
#
# Copyright (c) 2019 Packetcraft, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###################################################################################################

include $(ROOT_DIR)/platform/$(PLATFORM)/build/sources.mk
include $(ROOT_DIR)/platform/$(PLATFORM)/build/sources_ll.mk

#--------------------------------------------------------------------------------------------------
# 	Libraries
#--------------------------------------------------------------------------------------------------

INC_DIRS += \
	$(CONTROLLER_ROOT)/include/common \
	$(CONTROLLER_ROOT)/include/ble \
	$(WSF_ROOT)/include

#--------------------------------------------------------------------------------------------------
# 	Startup files
#--------------------------------------------------------------------------------------------------

C_FILES += \
	$(ROOT_DIR)/projects/controller/ble4-ctr/main.c
