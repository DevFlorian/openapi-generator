/**
 * OpenAPI Petstore
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The FileSchemaTestClass model module.
 * @module model/FileSchemaTestClass
 * @version 1.0.0
 */
class FileSchemaTestClass {
    /**
     * Constructs a new <code>FileSchemaTestClass</code>.
     * @alias module:model/FileSchemaTestClass
     */
    constructor() { 
        
        FileSchemaTestClass.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FileSchemaTestClass</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FileSchemaTestClass} obj Optional instance to populate.
     * @return {module:model/FileSchemaTestClass} The populated <code>FileSchemaTestClass</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FileSchemaTestClass();

            if (data.hasOwnProperty('file')) {
                obj['file'] = File.constructFromObject(data['file']);
            }
            if (data.hasOwnProperty('files')) {
                obj['files'] = ApiClient.convertToType(data['files'], [File]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FileSchemaTestClass</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FileSchemaTestClass</code>.
     */
    static validateJSON(data) {
        // validate the optional field `file`
        if (data['file']) { // data not null
          File.validateJSON(data['file']);
        }
        if (data['files']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['files'])) {
                throw new Error("Expected the field `files` to be an array in the JSON data but got " + data['files']);
            }
            // validate the optional field `files` (array)
            for (const item of data['files']) {
                File.validateJsonObject(item);
            };
        }

        return true;
    }


}



/**
 * @member {File} file
 */
FileSchemaTestClass.prototype['file'] = undefined;

/**
 * @member {Array.<File>} files
 */
FileSchemaTestClass.prototype['files'] = undefined;






export default FileSchemaTestClass;

