/*
 * Ory APIs
 * Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 
 *
 * The version of the OpenAPI document: v0.0.1-alpha.42
 * Contact: support@ory.sh
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package sh.ory.api;

import sh.ory.ApiException;
import sh.ory.model.GenericError;
import sh.ory.model.Project;
import sh.ory.model.ProjectPatch;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for V0alpha0Api
 */
@Ignore
public class V0alpha0ApiTest {

    private final V0alpha0Api api = new V0alpha0Api();

    
    /**
     * Create a Project
     *
     * Creates a new project.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void createProjectTest() throws ApiException {
        ProjectPatch projectPatch = null;
        Project response = api.createProject(projectPatch);

        // TODO: test validations
    }
    
    /**
     * Get a Project
     *
     * Get a projects you have access to by its ID.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getProjectTest() throws ApiException {
        String projectId = null;
        Project response = api.getProject(projectId);

        // TODO: test validations
    }
    
    /**
     * List All Projects
     *
     * Lists all projects you have access to.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void listProjectsTest() throws ApiException {
        List<Project> response = api.listProjects();

        // TODO: test validations
    }
    
    /**
     * Update a Project
     *
     * Creates a new configuration revision for a project.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void updateProjectTest() throws ApiException {
        String projectId = null;
        ProjectPatch projectPatch = null;
        Project response = api.updateProject(projectId, projectPatch);

        // TODO: test validations
    }
    
}
