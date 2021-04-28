/*
 * Ory Kratos API
 *
 * Documentation for all public and administrative Ory Kratos APIs. Public and administrative APIs are exposed on different ports. Public APIs can face the public internet without any protection while administrative APIs should never be exposed without prior authorization. To protect the administative API port you should use something like Nginx, Ory Oathkeeper, or any other technology capable of authorizing incoming requests. 
 *
 * The version of the OpenAPI document: v0.0.0-alpha.38
 * Contact: hi@ory.sh
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */


using Xunit;

using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;
using Ory.Kratos.Client.Api;
using Ory.Kratos.Client.Model;
using Ory.Kratos.Client.Client;
using System.Reflection;
using Newtonsoft.Json;

namespace Ory.Kratos.Client.Test.Model
{
    /// <summary>
    ///  Class for testing KratosSubmitSelfServiceRegistrationFlow
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by OpenAPI Generator (https://openapi-generator.tech).
    /// Please update the test case below to test the model.
    /// </remarks>
    public class KratosSubmitSelfServiceRegistrationFlowTests : IDisposable
    {
        // TODO uncomment below to declare an instance variable for KratosSubmitSelfServiceRegistrationFlow
        //private KratosSubmitSelfServiceRegistrationFlow instance;

        public KratosSubmitSelfServiceRegistrationFlowTests()
        {
            // TODO uncomment below to create an instance of KratosSubmitSelfServiceRegistrationFlow
            //instance = new KratosSubmitSelfServiceRegistrationFlow();
        }

        public void Dispose()
        {
            // Cleanup when everything is done.
        }

        /// <summary>
        /// Test an instance of KratosSubmitSelfServiceRegistrationFlow
        /// </summary>
        [Fact]
        public void KratosSubmitSelfServiceRegistrationFlowInstanceTest()
        {
            // TODO uncomment below to test "IsType" KratosSubmitSelfServiceRegistrationFlow
            //Assert.IsType<KratosSubmitSelfServiceRegistrationFlow>(instance);
        }


        /// <summary>
        /// Test the property 'CsrfToken'
        /// </summary>
        [Fact]
        public void CsrfTokenTest()
        {
            // TODO unit test for the property 'CsrfToken'
        }
        /// <summary>
        /// Test the property 'Password'
        /// </summary>
        [Fact]
        public void PasswordTest()
        {
            // TODO unit test for the property 'Password'
        }
        /// <summary>
        /// Test the property 'Traits'
        /// </summary>
        [Fact]
        public void TraitsTest()
        {
            // TODO unit test for the property 'Traits'
        }

    }

}
