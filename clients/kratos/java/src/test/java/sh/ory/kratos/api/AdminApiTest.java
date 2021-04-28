/*
 * Ory Kratos API
 * Documentation for all public and administrative Ory Kratos APIs. Public and administrative APIs are exposed on different ports. Public APIs can face the public internet without any protection while administrative APIs should never be exposed without prior authorization. To protect the administative API port you should use something like Nginx, Ory Oathkeeper, or any other technology capable of authorizing incoming requests. 
 *
 * The version of the OpenAPI document: v0.0.0-alpha.38
 * Contact: hi@ory.sh
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package sh.ory.kratos.api;

import sh.ory.kratos.ApiException;
import sh.ory.kratos.model.CreateIdentity;
import sh.ory.kratos.model.CreateRecoveryLink;
import sh.ory.kratos.model.ErrorContainer;
import sh.ory.kratos.model.GenericError;
import sh.ory.kratos.model.Identity;
import sh.ory.kratos.model.InlineResponse200;
import sh.ory.kratos.model.InlineResponse2001;
import sh.ory.kratos.model.InlineResponse503;
import sh.ory.kratos.model.LoginFlow;
import sh.ory.kratos.model.RecoveryFlow;
import sh.ory.kratos.model.RecoveryLink;
import sh.ory.kratos.model.RegistrationFlow;
import sh.ory.kratos.model.SettingsFlow;
import sh.ory.kratos.model.UpdateIdentity;
import sh.ory.kratos.model.VerificationFlow;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for AdminApi
 */
@Ignore
public class AdminApiTest {

    private final AdminApi api = new AdminApi();

    
    /**
     * Create an Identity
     *
     * This endpoint creates an identity. It is NOT possible to set an identity&#39;s credentials (password, ...) using this method! A way to achieve that will be introduced in the future.  Learn how identities work in [Ory Kratos&#39; User And Identity Model Documentation](https://www.ory.sh/docs/next/kratos/concepts/identity-user-model).
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void createIdentityTest() throws ApiException {
        CreateIdentity createIdentity = null;
        Identity response = api.createIdentity(createIdentity);

        // TODO: test validations
    }
    
    /**
     * Create a Recovery Link
     *
     * This endpoint creates a recovery link which should be given to the user in order for them to recover (or activate) their account.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void createRecoveryLinkTest() throws ApiException {
        CreateRecoveryLink createRecoveryLink = null;
        RecoveryLink response = api.createRecoveryLink(createRecoveryLink);

        // TODO: test validations
    }
    
    /**
     * Delete an Identity
     *
     * Calling this endpoint irrecoverably and permanently deletes the identity given its ID. This action can not be undone. This endpoint returns 204 when the identity was deleted or when the identity was not found, in which case it is assumed that is has been deleted already.  Learn how identities work in [Ory Kratos&#39; User And Identity Model Documentation](https://www.ory.sh/docs/next/kratos/concepts/identity-user-model).
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void deleteIdentityTest() throws ApiException {
        String id = null;
        api.deleteIdentity(id);

        // TODO: test validations
    }
    
    /**
     * Get an Identity
     *
     * Learn how identities work in [Ory Kratos&#39; User And Identity Model Documentation](https://www.ory.sh/docs/next/kratos/concepts/identity-user-model).
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getIdentityTest() throws ApiException {
        String id = null;
        Identity response = api.getIdentity(id);

        // TODO: test validations
    }
    
    /**
     * 
     *
     * Get a Traits Schema Definition
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getSchemaTest() throws ApiException {
        String id = null;
        Object response = api.getSchema(id);

        // TODO: test validations
    }
    
    /**
     * Get User-Facing Self-Service Errors
     *
     * This endpoint returns the error associated with a user-facing self service errors.  This endpoint supports stub values to help you implement the error UI:  &#x60;?error&#x3D;stub:500&#x60; - returns a stub 500 (Internal Server Error) error.  More information can be found at [Ory Kratos User User Facing Error Documentation](https://www.ory.sh/docs/kratos/self-service/flows/user-facing-errors).
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getSelfServiceErrorTest() throws ApiException {
        String error = null;
        ErrorContainer response = api.getSelfServiceError(error);

        // TODO: test validations
    }
    
    /**
     * Get Login Flow
     *
     * This endpoint returns a login flow&#39;s context with, for example, error details and other information.  More information can be found at [Ory Kratos User Login and User Registration Documentation](https://www.ory.sh/docs/next/kratos/self-service/flows/user-login-user-registration).
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getSelfServiceLoginFlowTest() throws ApiException {
        String id = null;
        LoginFlow response = api.getSelfServiceLoginFlow(id);

        // TODO: test validations
    }
    
    /**
     * Get information about a recovery flow
     *
     * This endpoint returns a recovery flow&#39;s context with, for example, error details and other information.  More information can be found at [Ory Kratos Account Recovery Documentation](../self-service/flows/account-recovery.mdx).
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getSelfServiceRecoveryFlowTest() throws ApiException {
        String id = null;
        RecoveryFlow response = api.getSelfServiceRecoveryFlow(id);

        // TODO: test validations
    }
    
    /**
     * Get Registration Flow
     *
     * This endpoint returns a registration flow&#39;s context with, for example, error details and other information.  More information can be found at [Ory Kratos User Login and User Registration Documentation](https://www.ory.sh/docs/next/kratos/self-service/flows/user-login-user-registration).
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getSelfServiceRegistrationFlowTest() throws ApiException {
        String id = null;
        RegistrationFlow response = api.getSelfServiceRegistrationFlow(id);

        // TODO: test validations
    }
    
    /**
     * Get Settings Flow
     *
     * When accessing this endpoint through Ory Kratos&#39; Public API you must ensure that either the Ory Kratos Session Cookie or the Ory Kratos Session Token are set. The public endpoint does not return 404 status codes but instead 403 or 500 to improve data privacy.  You can access this endpoint without credentials when using Ory Kratos&#39; Admin API.  More information can be found at [Ory Kratos User Settings &amp; Profile Management Documentation](../self-service/flows/user-settings).
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getSelfServiceSettingsFlowTest() throws ApiException {
        String id = null;
        SettingsFlow response = api.getSelfServiceSettingsFlow(id);

        // TODO: test validations
    }
    
    /**
     * Get Verification Flow
     *
     * This endpoint returns a verification flow&#39;s context with, for example, error details and other information.  More information can be found at [Ory Kratos Email and Phone Verification Documentation](https://www.ory.sh/docs/kratos/selfservice/flows/verify-email-account-activation).
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getSelfServiceVerificationFlowTest() throws ApiException {
        String id = null;
        VerificationFlow response = api.getSelfServiceVerificationFlow(id);

        // TODO: test validations
    }
    
    /**
     * Return Running Software Version.
     *
     * This endpoint returns the version of Ory Kratos.  If the service supports TLS Edge Termination, this endpoint does not require the &#x60;X-Forwarded-Proto&#x60; header to be set.  Be aware that if you are running multiple nodes of this service, the version will never refer to the cluster state, only to a single instance.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getVersionTest() throws ApiException {
        InlineResponse2001 response = api.getVersion();

        // TODO: test validations
    }
    
    /**
     * Check HTTP Server Status
     *
     * This endpoint returns a HTTP 200 status code when Ory Kratos is accepting incoming HTTP requests. This status does currently not include checks whether the database connection is working.  If the service supports TLS Edge Termination, this endpoint does not require the &#x60;X-Forwarded-Proto&#x60; header to be set.  Be aware that if you are running multiple nodes of this service, the health status will never refer to the cluster state, only to a single instance.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void isAliveTest() throws ApiException {
        InlineResponse200 response = api.isAlive();

        // TODO: test validations
    }
    
    /**
     * Check HTTP Server and Database Status
     *
     * This endpoint returns a HTTP 200 status code when Ory Kratos is up running and the environment dependencies (e.g. the database) are responsive as well.  If the service supports TLS Edge Termination, this endpoint does not require the &#x60;X-Forwarded-Proto&#x60; header to be set.  Be aware that if you are running multiple nodes of Ory Kratos, the health status will never refer to the cluster state, only to a single instance.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void isReadyTest() throws ApiException {
        InlineResponse200 response = api.isReady();

        // TODO: test validations
    }
    
    /**
     * List Identities
     *
     * Lists all identities. Does not support search at the moment.  Learn how identities work in [Ory Kratos&#39; User And Identity Model Documentation](https://www.ory.sh/docs/next/kratos/concepts/identity-user-model).
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void listIdentitiesTest() throws ApiException {
        Long perPage = null;
        Long page = null;
        List<Identity> response = api.listIdentities(perPage, page);

        // TODO: test validations
    }
    
    /**
     * Get snapshot metrics from the Hydra service. If you&#39;re using k8s, you can then add annotations to your deployment like so:
     *
     * &#x60;&#x60;&#x60; metadata: annotations: prometheus.io/port: \&quot;4434\&quot; prometheus.io/path: \&quot;/metrics/prometheus\&quot; &#x60;&#x60;&#x60;
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void prometheusTest() throws ApiException {
        api.prometheus();

        // TODO: test validations
    }
    
    /**
     * Update an Identity
     *
     * This endpoint updates an identity. It is NOT possible to set an identity&#39;s credentials (password, ...) using this method! A way to achieve that will be introduced in the future.  The full identity payload (except credentials) is expected. This endpoint does not support patching.  Learn how identities work in [Ory Kratos&#39; User And Identity Model Documentation](https://www.ory.sh/docs/next/kratos/concepts/identity-user-model).
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void updateIdentityTest() throws ApiException {
        String id = null;
        UpdateIdentity updateIdentity = null;
        Identity response = api.updateIdentity(id, updateIdentity);

        // TODO: test validations
    }
    
}
