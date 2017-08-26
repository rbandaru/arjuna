/*******************************************************************************
 * Copyright 2015-16 AutoCognite Testing Research Pvt Ltd
 * 
 * Website: www.AutoCognite.com
 * Email: support [at] autocognite.com
 * 
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *   http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 ******************************************************************************/
package pvt.unitee.reporter.lib.writer.json;

import org.apache.log4j.Logger;

import pvt.batteries.config.Batteries;
import pvt.unitee.enums.ArjunaProperty;
import pvt.unitee.reporter.lib.ignored.IgnoredTest;
import pvt.unitee.reporter.lib.test.TestResult;

public class JsonIgnoredTestWriter extends JsonResultWriter<IgnoredTest> {
	private Logger logger = Logger.getLogger(Batteries.getCentralLogName());
	JsonConsolidatedTestResultWriter childWriter = null;
	
	public JsonIgnoredTestWriter() throws Exception{
		super(Batteries.value(ArjunaProperty.DIRECTORY_PROJECT_RUNID_REPORT_JSON_RAW_IGNOREDTESTS).asString());
		childWriter = new JsonConsolidatedTestResultWriter();
	}
	
	public void update(IgnoredTest reportable) throws Exception {
		String jsonString = reportable.asJsonObject().toString();
		super.update(this.createFileID(String.valueOf(reportable.hashCode())), jsonString);
		childWriter.update(jsonString);
	}
	
	public void setUp() throws Exception{
		super.setUp();
		childWriter.setUp();
	}

	public void tearDown() throws Exception{
		super.tearDown();
		childWriter.tearDown();
	}
}